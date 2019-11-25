package com.example.my_recipes;

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
import android.widget.EditText;

import org.json.JSONException;
import org.json.JSONObject;

import java.util.concurrent.ExecutionException;

public class Login extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);
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
        Button login = (Button) findViewById(R.id.button5);
        login.setOnClickListener(new View.OnClickListener() {
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
        String name,from,to;
        JSONObject j = new JSONObject();
        EditText password_edit = (EditText) findViewById(R.id.editText11);
        EditText username_edit = (EditText) findViewById(R.id.editText12);

        try {
            j.put("username",username_edit.getText().toString());
            j.put("password",password_edit.getText().toString());
        } catch (JSONException e) {
            e.printStackTrace();
        }

        from = "";
        to ="";
        AsyncTask<String, String, String> res = new MainActivity.background().execute("http://24.133.185.104:4545/login",j.toString(),from,to);
        String s = res.get();
        System.out.println("abssss:"+s);

        System.out.println("abcccc:"+s.equals("True"));
        JSONObject jsonObject = new JSONObject(s);
        if(jsonObject.get("result").toString().equals("True")){
            System.out.println(getIsLogin());
            setIsLogin(true);
            setUsername(username_edit.toString());
            System.out.println(getIsLogin());

            Intent intent;
            intent = new Intent(this, Search.class);
            startActivity(intent);
        }
        else{
            Intent intent;
            intent = new Intent(this, MainActivity.class);
            startActivity(intent);
        }
        System.out.println(s);
    }

    public void setIsLogin(Boolean b){
        SharedPreferences pref = getApplicationContext().getSharedPreferences("MyPref", MODE_PRIVATE);
        SharedPreferences.Editor editor = pref.edit();
        editor.putBoolean("islogin", b);
        editor.commit();
    }


    public Boolean getIsLogin(){
        SharedPreferences pref = getApplicationContext().getSharedPreferences("MyPref", MODE_PRIVATE);
        Boolean isConfirmed=pref.getBoolean("islogin", false);         // getting String
        return isConfirmed;
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
