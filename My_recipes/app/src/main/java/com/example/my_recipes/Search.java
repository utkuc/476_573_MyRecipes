package com.example.my_recipes;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.AsyncTask;
import android.os.Bundle;

import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.widget.Toolbar;

import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.AutoCompleteTextView;
import android.widget.Button;
import android.widget.TextView;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.concurrent.ExecutionException;

public class Search extends AppCompatActivity {

    ArrayList<String> arr = new ArrayList<>();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_search);
        Toolbar toolbar = findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);



        ArrayList<String> arr = new ArrayList<>();
        AutoCompleteTextView autoTextView = (AutoCompleteTextView) findViewById(R.id.autoCompleteTextView);
        TextView textView = (TextView) findViewById(R.id.textView);


        String[] str = {"lentils","basmati rice","ground beef","dates","raisins","saffron","onions","cooking oil","salt","black pepper","maple syrup","blueberries","of fresh mint","semi-sweet chocolate chips","smooth peanut butter","graham cracker crumbs","confectioners' sugar","vanilla","fudge cake mix","eggs","oil","water","brown sugar","flour","dried mustard","cinnamon","dry sherry","vinegar","flounder fillets","parmesan cheese","low-fat mayonnaise","green onions","dry breadcrumbs","dried basil","dried oregano","pepper","long grain and wild rice blend","green peppers","onion","chunky tomato pasta sauce","italian-style diced tomatoes","beef broth","ham bone","potatoes","ham","garlic cloves","butter","milk","shredded cheddar cheese","salt and pepper","vegetable oil cooking spray","chicken breast halves","paprika","red onion","sweet green pepper","sweet red pepper","jalapeno pepper","fresh ginger","acorn squash","fresh tomatoes","chicken stock","cornstarch","yellow cornmeal","light brown sugar","ginger","baking soda","buttermilk","coconut","mashed sweet potato","egg","instant yeast","oat flour","sugar","sea salt","dried rosemary","dried cranberries","beef","salsa","yellow onion","garlic","jalapeno","poblano chile","red sweet bell peppers","cremini mushroom","monterey jack cheese","phyllo dough","olive oil","guacamole","sour cream","lettuce","black olives","cheese","diced green chilis","angel food cake","sweetened condensed milk","cold water","almond extract","vanilla instant pudding mix","whipping cream","cherry pie filling","yukon gold potatoes","shallots","all-purpose flour","1% low-fat milk","asiago cheese","fresh chives","fresh ground pepper","bacon","fresh parmesan cheese","lean beef chuck roast","baking potatoes","carrots","celery ribs","parsnip","bay leaves","dried thyme leaves","chicken","plain yogurt","almonds","pine nuts","parsley","long grain white rice","pita bread","active dry yeast","shortening","ground mace","lemon extract","vanilla extract","vegetable oil","cumin seed","dry white wine","fish stock","live lobsters","carrot","celery","cognac","tomatoes","thyme","ground red pepper","heavy cream","breadcrumbs","onion powder","garlic salt","chicken wings","white sugar","warm water","pecans","ground cinnamon","catfish fillets","margarine","cajun seasoning","medium shrimp","blue crab meat","heavy whipping cream","unsalted butter","seafood stock","fresh spinach","red leaf lettuce","romaine lettuce","red pepper","artichokes","pepperoncini peppers","plum tomatoes","herbed croutons","parmigiano-reggiano cheese","canola oil","fresh thyme","dry mustard","eggplant","stewing veal","ground cumin","ground allspice","ground coriander","cayenne pepper","diced tomatoes","tomato paste","dry red wine","lemon juice","kalamata olive","flat leaf parsley","potato starch","lemons, zest of","dried chili pepper flakes","dijon mustard","soy sauce","ramen noodles","snow peas","red bell pepper","apricot preserves","toasted sesame seeds","chicken broth","extra virgin olive oil","montreal chicken seasoning","fresh ground black pepper","boneless skinless chicken breasts","honey","oatmeal","cottage cheese","agave nectar","maple extract","skinless chicken breasts","green bell pepper","chicken stock cube","cayenne","cumin","corn","salmon fillets","kosher salt","fresh dill","capers","raspberry vinegar"};
        String text = str[0];

        ArrayAdapter<String> adapter = new ArrayAdapter<String>(this, android.R.layout.select_dialog_item, str);
        autoTextView.setThreshold(1); //will start working from first character
        autoTextView.setAdapter(adapter);
        Button add = (Button)findViewById(R.id.add_ing);
        add.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                System.out.println("faaaa");
                addAction();
            }
        });
        Button remove = (Button)findViewById(R.id.button);
        remove.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                removeAction();
            }
        });
        Button clear = (Button)findViewById(R.id.button8);
        clear.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                clearAction();
            }
        });
        Button search = (Button)findViewById(R.id.button6);
        search.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                try {
                    searchAction();
                } catch (ExecutionException e) {
                    e.printStackTrace();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        });
        Button category = (Button)findViewById(R.id.button9);
        category.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

            }
        });
        Button logout = (Button)findViewById(R.id.logout);
        logout.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                logoutAction();
            }
        });
    }
    public void addAction(){
        System.out.println("adsadas");
        AutoCompleteTextView autoTextView = (AutoCompleteTextView) findViewById(R.id.autoCompleteTextView);
        TextView textView = (TextView) findViewById(R.id.textView);
        String str = autoTextView.getText().toString();
        System.out.println(str);
        if (str.length()>1){
            arr.add(str);
            autoTextView.setText("");
            textView.setText(arr.toString());
        }
    }
    public void removeAction(){
        System.out.println("adsadas");
        AutoCompleteTextView autoTextView = (AutoCompleteTextView) findViewById(R.id.autoCompleteTextView);
        TextView textView = (TextView) findViewById(R.id.textView);
        String str = autoTextView.getText().toString();
        System.out.println(str);
        arr.remove(arr.size()-1);
        autoTextView.setText("");
        textView.setText(arr.toString());

    }
    public void clearAction(){
        System.out.println("adsadas");
        AutoCompleteTextView autoTextView = (AutoCompleteTextView) findViewById(R.id.autoCompleteTextView);
        TextView textView = (TextView) findViewById(R.id.textView);
        String str = autoTextView.getText().toString();
        System.out.println(str);
        arr = new ArrayList<>();
        autoTextView.setText("");
        textView.setText(arr.toString());
    }
    public void searchAction() throws ExecutionException, InterruptedException {
        String name,from,to;
        JSONObject j = new JSONObject();
        //String keywords = arr.toString();
        JSONArray keywords = new JSONArray(arr);
        System.out.println(keywords);
        try {
            j.put("keywords",keywords);
            j.put("categories","");
        } catch (JSONException e) {
            e.printStackTrace();
        }

        from = "";
        to ="";
        AsyncTask<String, String, String> res = new MainActivity.background().execute("http://24.133.185.104:4545/get_search_result_recipes",j.toString(),from,to);

        String s = "";
        s = res.get();

        System.out.println("response"+s);
        Intent intent = new Intent(getBaseContext(), Recipes.class);
        intent.putExtra("recipes", s);
        startActivity(intent);
    }
    public void logoutAction(){
        setIsLogin(false);
        Intent intent;
        intent = new Intent(this, MainActivity.class);
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

}
