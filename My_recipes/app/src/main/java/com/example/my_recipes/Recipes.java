package com.example.my_recipes;

import android.content.Intent;
import android.os.Build;
import android.os.Bundle;

import com.google.android.material.floatingactionbutton.FloatingActionButton;
import com.google.android.material.snackbar.Snackbar;

import androidx.annotation.RequiresApi;
import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.widget.Toolbar;

import android.view.View;
import android.widget.LinearLayout;
import android.widget.TextView;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;


public class Recipes extends AppCompatActivity {
    LinearLayout linearLayout;
    @RequiresApi(api = Build.VERSION_CODES.KITKAT)
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_recipes);
        Toolbar toolbar = findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        FloatingActionButton fab = findViewById(R.id.fab);
        fab.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Snackbar.make(view, "Replace with your own action", Snackbar.LENGTH_LONG)
                        .setAction("Action", null).show();
            }
        });
        String json_response = getIntent().getStringExtra("recipes");
        linearLayout = findViewById(R.id.linearlayout);


        TextView titleView = new TextView(this);




        System.out.println("RESP:"+json_response);
        try {
            JSONObject jsonObject = new JSONObject(json_response);
            JSONArray arr;
            arr = new JSONArray(jsonObject.get("recipes").toString());
            for (int i = 0; i<30 &&i < arr.length(); i++){
                final String recipe_id = arr.getJSONObject(i).get("recipe_id").toString();
                System.out.println(recipe_id);
                String title = arr.getJSONObject(i).get("title").toString();
                System.out.println(title);
                String calories = arr.getJSONObject(i).get("calories").toString();
                System.out.println(calories);
                String ingredients = arr.getJSONObject(i).get("ingredients").toString();
                System.out.println(ingredients);
                LinearLayout recipebox = new LinearLayout(this);
                recipebox.setOrientation(LinearLayout.VERTICAL);
                recipebox.setLayoutParams(new LinearLayout.LayoutParams(LinearLayout.LayoutParams.FILL_PARENT, LinearLayout.LayoutParams.FILL_PARENT));
                TextView textView = new TextView(this);
                textView.setText(title);
                textView.setTextSize(24);
                recipebox.addView(textView);

                textView = new TextView(this);
                textView.setText(calories);
                recipebox.addView(textView);

                textView = new TextView(this);
                textView.setText(ingredients);
                recipebox.addView(textView);

                textView = new TextView(this);
                textView.setText(recipe_id);
                textView.setTextSize(1);
                textView.setVisibility(View.INVISIBLE);
                recipebox.addView(textView);

                recipebox.setOnClickListener(new View.OnClickListener() {
                    @Override
                    public void onClick(View v) {
                        openRecipePage(recipe_id);
                    }
                });


                linearLayout.addView(recipebox);


            }
            TextView textView = (TextView) findViewById(R.id.textView3);
            String str = arr.getJSONObject(0).get("title").toString();
            textView.setText(str);
        } catch (JSONException e) {
            e.printStackTrace();
        }

    }
    public void openRecipePage(String recipe_id){
        Intent intent = new Intent(getBaseContext(), Recipe_page.class);
        intent.putExtra("recipe_id", recipe_id);
        startActivity(intent);

    }
}
