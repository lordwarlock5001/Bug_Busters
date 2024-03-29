package com.example.riya.myapplication;

import android.Manifest;
import android.content.Context;
import android.content.Intent;
import android.support.v4.app.ActivityCompat;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.TextView;

public class Welcome extends AppCompatActivity {
    public static Context mainActivityContext;

    static String postUrl = "http://192.168.16.102:5000";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        setContentView(R.layout.activity_welcome);

        ActivityCompat.requestPermissions(Welcome.this, new String[]{Manifest.permission.INTERNET}, 0);

        mainActivityContext = this;
    }

    public void login(View v) {
        Intent intent = new Intent(this, Login.class);
        startActivityForResult(intent, 2);
    }

    public void register(View v) {
        Intent intent = new Intent(this, Register.class);
        startActivity(intent);
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        TextView responseText = findViewById(R.id.textView4);
        if (requestCode == 2) { // Login
            responseText.setText("Successful Login.");
        } else {
            responseText.setText("Invalid or no data entered. Please try again.");
        }
    }

}