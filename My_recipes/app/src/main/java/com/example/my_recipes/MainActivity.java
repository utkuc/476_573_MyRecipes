package com.example.my_recipes;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.AsyncTask;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.HashMap;
import java.util.Map;
import java.util.concurrent.ExecutionException;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        System.out.println("login "+getIsLogin());
        if(getIsLogin()){
            Intent intent;
            intent = new Intent(this, Search.class);
            startActivity(intent);
        }
        else{
            setContentView(R.layout.activity_main);
        }

        Button login = (Button) findViewById(R.id.login);
        login.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                openLogin();
            }
        });

        Button signup = (Button) findViewById(R.id.signup);
        signup.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openSignup();
            }
        });
        Button search = (Button) findViewById(R.id.SearchMain);
        search.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openSearch();
            }
        });

    }
    public void openLogin(){
        Intent intent;
        intent = new Intent(this, Login.class);
        startActivity(intent);
    }
    public void openSignup(){
        Intent intent;
        intent = new Intent(this, Signup.class);
        startActivity(intent);
    }
    public void openSearch(){
        Intent intent;
        intent = new Intent(this, Search.class);
        startActivity(intent);
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

    public Boolean getIsAdmin(){
        SharedPreferences pref = getApplicationContext().getSharedPreferences("MyPref", MODE_PRIVATE);
        Boolean isConfirmed=pref.getBoolean("isadmin", false);         // getting String
        return isConfirmed;
    }
    public void setAdmin(Boolean b){
        SharedPreferences pref = getApplicationContext().getSharedPreferences("MyPref", MODE_PRIVATE);
        SharedPreferences.Editor editor = pref.edit();
        editor.putBoolean("isadmin", b);
        editor.commit();
    }


    public void post_json_request() throws ExecutionException, InterruptedException {
        String name,from,to;
        JSONObject j = new JSONObject();

        try {
            j.put("mustafa","tokmak");
            j.put("mustafa2","tokmak2");
            j.put("mustafa3","tokmak3");
        } catch (JSONException e) {
            e.printStackTrace();
        }

        from = "";
        to ="";
        AsyncTask<String, String, String> res = new background().execute("https://hookb.in/XkxlYGbDBzuKnqojMq0g",j.toString(),from,to);
        String s = res.get();
        System.out.println(s);
    }
    static class background extends AsyncTask<String,String,String>{
        protected String doInBackground (String ... params){
            HttpURLConnection connection = null;
            BufferedReader bufferedReader = null;
            String file = "";

            if(params.length>1){
                try{
                    URL url = new URL(params[0]);
                    Log.d("adsgfdhfsadurl",params[0]);

                    JSONObject jsonObject;
                    jsonObject = new JSONObject(params[1]);

                    Log.i("JSON", jsonObject.toString());


                    connection = (HttpURLConnection) url.openConnection();
                    connection.setRequestMethod("POST");
                    connection.setRequestProperty("Content-Type", "application/json");
                    //connection.setRequestProperty("Accept","application/json");
                    //connection.setRequestProperty("Authentication","Bearer Q70lWlPwbjFQDWHcPkvZSrx1RTReqvu9DuW/Ff1JO1cZNhVb7d5ekJ2ra0eJ4PF1au7HtX3NTxIiyFwXEORxow==");

                    connection.setDoInput(true);
                    connection.setDoOutput(true);
                    connection.connect();





                    DataOutputStream dos = new DataOutputStream(connection.getOutputStream());
                    dos.writeBytes(jsonObject.toString());
                    dos.flush();
                    dos.close();

                    BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()));
                    StringBuilder sb = new StringBuilder();
                    String line = null;
                    while((line = reader.readLine()) != null)
                    {
                        // Append server response in string
                        sb.append(line + "\n");
                    }
                    String text = sb.toString();
                    reader.close();
                    System.out.println(text);

                    JSONObject jsonResponse = new JSONObject(text);

                    file = jsonResponse.toString();


                    //String result = jsonResponse.get("Scored Labels");
                    //System.out.println(result);


                    Log.i("STATUS", String.valueOf(connection.getResponseCode()));
                    Log.i("MSG" , connection.getResponseMessage());

                    connection.disconnect();


                    //file = connection.getResponseMessage();
                }catch (Exception e){

                }
                return file;
            }
            else{
                try{
                    URL url = new URL(params[0]);
                    Log.d("url",params[0]);

                    connection = (HttpURLConnection) url.openConnection();
                    connection.connect();
                    InputStream inputStream = connection.getInputStream();
                    bufferedReader = new BufferedReader(new InputStreamReader(inputStream));
                    String line;
                    while ((line = bufferedReader.readLine()) != null){
                        Log.d("line:",line);
                        file += line;
                    }
                }catch (Exception e){

                }
                return file;
            }

        }

    }
}
