package com.example.riya.myapplication;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.IOException;

import okhttp3.Call;
import okhttp3.Callback;
import okhttp3.MediaType;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.RequestBody;
import okhttp3.Response;

public class Register extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_register);
    }
    public void tomainpage(View v) {
        Intent intent = new Intent(this, MapsActivity.class);
        startActivity(intent);
    }

    public void register(View v) {
        EditText usernameView = findViewById(R.id.editText4);
        EditText firstNameView = findViewById(R.id.editText);
        EditText lastNameView = findViewById(R.id.editText2);
        EditText passwordView = findViewById(R.id.editText5);
        EditText mobileView = findViewById(R.id.editText3);
        EditText confirmView = findViewById(R.id.editText7);
        final Button register = findViewById(R.id.button2);

        String username = usernameView.getText().toString().trim();
        String firstName = firstNameView.getText().toString().trim();
        String lastName = lastNameView.getText().toString().trim();
        String mobileNo = mobileView.getText().toString().trim();
        String password = passwordView.getText().toString().trim();



        if (firstName.length() == 0 || lastName.length() == 0 || mobileNo.length() == 0 || username.length() == 0 || password.length() == 0) {
            Toast.makeText(getApplicationContext(), "Something is wrong. Please check your inputs.", Toast.LENGTH_LONG).show();
        } else {
            JSONObject registrationForm = new JSONObject();
            try {
                registrationForm.put("subject", "register");
                registrationForm.put("firstname", firstName);
                registrationForm.put("lastname", lastName);
                registrationForm.put("mobileno", mobileNo);
                registrationForm.put("username", username);
                registrationForm.put("password", password);
            } catch (JSONException e) {
                e.printStackTrace();
            }

            RequestBody body = RequestBody.create(MediaType.parse("application/json; charset=utf-8"), registrationForm.toString());

            postRequest(Welcome.postUrl, body);
        }
        register.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {


                startActivity(new Intent(Register.this,Login.class));

            }
        });
    }

    public void postRequest(String postUrl, RequestBody postBody) {
        OkHttpClient client = new OkHttpClient();

        final Request request = new Request.Builder()
                .url(postUrl)
                .post(postBody)
                .header("Accept", "application/json")
                .header("Content-Type", "application/json")
                .build();

        client.newCall(request).enqueue(new Callback() {
            @Override
            public void onFailure(Call call, IOException e) {
                call.cancel();
                Log.d("FAIL", e.getMessage());

                runOnUiThread(new Runnable() {
                    @Override
                    public void run() {
                        TextView responseText = findViewById(R.id.textView5);
                        responseText.setText("Failed to Connect to Server. Please Try Again.");
                    }
                });
            }

            @Override
            public void onResponse(Call call, final Response response) {
                final TextView responseTextRegister = findViewById(R.id.textView9);
                try {
                    final String responseString = response.body().string().trim();
                    runOnUiThread(new Runnable() {
                        @Override
                        public void run() {
                            if (responseString.equals("success")) {
                                responseTextRegister.setText("Registration completed successfully.");
                                finish();
                            } else if (responseString.equals("username")) {
                                responseTextRegister.setText("Username already exists. Please chose another username.");
                            } else {
                                responseTextRegister.setText("Something went wrong. Please try again later.");
                            }
                        }
                    });
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        });
    }
}