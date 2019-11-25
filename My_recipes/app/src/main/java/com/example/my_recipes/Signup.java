package com.example.my_recipes;

import android.content.Intent;
import android.os.AsyncTask;
import android.os.Bundle;

import com.google.android.material.floatingactionbutton.FloatingActionButton;
import com.google.android.material.snackbar.Snackbar;

import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.widget.Toolbar;

import android.view.View;
import android.widget.Button;
import android.widget.EditText;

import org.json.JSONException;
import org.json.JSONObject;

import java.util.concurrent.ExecutionException;

public class Signup extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_signup);
        Toolbar toolbar = findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        Button signup = (Button) findViewById(R.id.button4);
        signup.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                try {
                    post_json_request();
                } catch (ExecutionException e) {
                    e.printStackTrace();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                } catch (JSONException e) {
                    e.printStackTrace();
                }
            }
        });


    }
    private void post_json_request() throws ExecutionException, InterruptedException, JSONException {
        String name, from, to;
        JSONObject j = new JSONObject();
        EditText email_edit = (EditText) findViewById(R.id.editText7);
        EditText username_edit = (EditText) findViewById(R.id.editText8);
        EditText password_edit = (EditText) findViewById(R.id.editText9);
        EditText name_edit = (EditText) findViewById(R.id.editText10);

        try {
            j.put("email", email_edit.getText().toString());
            j.put("username", username_edit.getText().toString());
            j.put("password", password_edit.getText().toString());
            j.put("name", name_edit.getText().toString());

        } catch (JSONException e) {
            e.printStackTrace();
        }

        from = "";
        to = "";
        AsyncTask<String, String, String> res = new MainActivity.background().execute("http://24.133.185.104:4545/sign_up", j.toString(), from, to);
        String s = res.get();
        Intent intent;
        intent = new Intent(this, MainActivity.class);
        startActivity(intent);
    }

}
