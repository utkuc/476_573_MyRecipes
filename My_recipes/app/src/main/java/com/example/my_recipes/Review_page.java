package com.example.my_recipes;

import android.content.Intent;
import android.os.AsyncTask;
import android.os.Build;
import android.os.Bundle;

import com.google.android.material.floatingactionbutton.FloatingActionButton;
import com.google.android.material.snackbar.Snackbar;

import androidx.annotation.RequiresApi;
import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.widget.Toolbar;

import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.LinearLayout;
import android.widget.RadioButton;
import android.widget.RadioGroup;
import android.widget.TextView;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;
import org.w3c.dom.Text;

import java.util.concurrent.ExecutionException;

public class Review_page extends AppCompatActivity {

    @RequiresApi(api = Build.VERSION_CODES.KITKAT)
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_review_page);
        Toolbar toolbar = findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);



        final String recipe_id = getIntent().getStringExtra("recipe_id");
        String title = getIntent().getStringExtra("title");

        TextView title_view = (TextView) findViewById(R.id.textView19);
        title_view.setText(title);

        //get reviews with recipe_id and list

        final Button submit = (Button) findViewById(R.id.reviews);
        submit.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                try {
                    submit_review(recipe_id);
                } catch (ExecutionException e) {
                    e.printStackTrace();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        });
        String reviews = "";
        try {
            reviews = get_reviews(recipe_id);
        } catch (ExecutionException e) {
            e.printStackTrace();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        JSONObject jsonObject = null;
        try {
            jsonObject = new JSONObject(reviews);
        } catch (JSONException e) {
            e.printStackTrace();
        }
        LinearLayout linearLayout = findViewById(R.id.linear_reviews);
        System.out.println(jsonObject.toString());
        try {
            JSONArray arr = new JSONArray(jsonObject.get("reviews").toString());
            for (int i = 0; i<30 &&i < arr.length(); i++){

                String username = arr.getJSONObject(i).get("username").toString();
                System.out.println(username);
                String rating = arr.getJSONObject(i).get("rating").toString();
                System.out.println(rating);
                String comment = arr.getJSONObject(i).get("comment").toString();
                System.out.println(comment);



                LinearLayout recipebox = new LinearLayout(this);
                recipebox.setOrientation(LinearLayout.VERTICAL);
                recipebox.setLayoutParams(new LinearLayout.LayoutParams(LinearLayout.LayoutParams.FILL_PARENT, LinearLayout.LayoutParams.FILL_PARENT));
                TextView textView = new TextView(this);

                textView.setText(username);
                recipebox.addView(textView);

                textView = new TextView(this);
                textView.setText(rating);
                recipebox.addView(textView);

                textView = new TextView(this);
                textView.setText(comment);
                recipebox.addView(textView);

                linearLayout.addView(recipebox);


            }
        } catch (JSONException e) {
            e.printStackTrace();
        }


    }
    public void submit_review(String recipe_id) throws ExecutionException, InterruptedException {
        String username = getIntent().getStringExtra("username");

        RadioGroup rg = (RadioGroup) findViewById(R.id.radioGroup);
        int selectedId = rg.getCheckedRadioButtonId();
        RadioButton rb = (RadioButton) findViewById(selectedId);
        String rating = rb.getText().toString();

        EditText editText = (EditText) findViewById(R.id.editText);
        String comment = editText.getText().toString();



        String name,from,to;
        JSONObject j = new JSONObject();

        try {
            j.put("recipe_id",recipe_id);

            j.put("username",username);
            j.put("comment",comment);
            j.put("rating",rating);

        } catch (JSONException e) {
            e.printStackTrace();
        }

        from = "";
        to ="";
        AsyncTask<String, String, String> res = new MainActivity.background().execute("http://24.133.185.104:4545/add_recipe_reviews_with_id",j.toString(),from,to);
        String s = res.get();
        System.out.println(s);
        Intent intent = new Intent(getBaseContext(), Review_page.class);
        startActivity(intent);




    }
    public String get_reviews(String recipe_id) throws ExecutionException, InterruptedException {
        String name,from,to;
        JSONObject j = new JSONObject();

        try {
            j.put("recipe_id",recipe_id);
        } catch (JSONException e) {
            e.printStackTrace();
        }

        from = "";
        to ="";
        AsyncTask<String, String, String> res = new MainActivity.background().execute("http://24.133.185.104:4545/get_recipe_reviews_with_id",j.toString(),from,to);
        String s = res.get();
        return s;
    }

}
