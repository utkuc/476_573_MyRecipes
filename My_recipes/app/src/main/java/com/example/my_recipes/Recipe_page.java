package com.example.my_recipes;

import android.app.job.JobScheduler;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.AsyncTask;
import android.os.Bundle;

import com.google.android.material.floatingactionbutton.FloatingActionButton;
import com.google.android.material.snackbar.Snackbar;

import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.widget.Toolbar;

import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.concurrent.ExecutionException;

public class Recipe_page extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_recipe_page);
        Toolbar toolbar = findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);



        final String recipe_id = getIntent().getStringExtra("recipe_id");
        String name,from,to;
        JSONObject j = new JSONObject();
        //String keywords = arr.toString();
        try {
            j.put("recipe_id",recipe_id);
        } catch (JSONException e) {
            e.printStackTrace();
        }

        from = "";
        to ="";
        AsyncTask<String, String, String> res = new MainActivity.background().execute("http://24.133.185.104:4545/get_recipe_with_id",j.toString(),from,to);

        String s = "";
        try {
            s = res.get();
        } catch (ExecutionException e) {
            e.printStackTrace();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        JSONObject jsonObject = null;
        try {
            jsonObject = new JSONObject(s);
        } catch (JSONException e) {
            e.printStackTrace();
        }
        String recipe_info ="";
        try {
            recipe_info = jsonObject.get("recipe_info").toString();
        } catch (JSONException e) {
            e.printStackTrace();
        }
        TextView textView2 = (TextView) findViewById(R.id.textView2);
        textView2.setText(recipe_info);

        Button reviews = (Button) findViewById(R.id.reviews);
        reviews.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openReviews(recipe_id,"recipe title");//TODO title ekle
            }
        });
        Button search_menu = (Button) findViewById(R.id.search_menu);
        search_menu.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openReviews(recipe_id,"recipe title");//TODO title ekle
            }
        });

    }
    public void openSearch(){
        Intent intent = new Intent(getBaseContext(), Search.class);
        startActivity(intent);
    }
    public void openReviews(String recipe_id,String title){
        Intent intent = new Intent(getBaseContext(), Review_page.class);
        intent.putExtra("recipe_id", recipe_id);
        intent.putExtra("username", getUsername());
        intent.putExtra("title", title);
        startActivity(intent);

    }

    public void setUsername(String b){
        SharedPreferences pref = getApplicationContext().getSharedPreferences("MyPref", MODE_PRIVATE);
        SharedPreferences.Editor editor = pref.edit();
        editor.putString("username", b);
        editor.commit();
    }


    public String getUsername(){
        SharedPreferences pref = getApplicationContext().getSharedPreferences("MyPref", MODE_PRIVATE);
        String username=pref.getString("username", "mustafa");         // getting String
        return username;
    }

}
