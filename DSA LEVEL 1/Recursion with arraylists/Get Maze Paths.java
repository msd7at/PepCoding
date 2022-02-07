// package com.leet;

import java.util.*;

//import java.io.*;
//import java.util.*;

import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {
    Scanner scn = new Scanner(System.in);
    int n = scn.nextInt();
    int m = scn.nextInt();
    ArrayList< String> paths = getMazePaths(1, 1, n, m);
    System.out.println(paths);
    }

    // sr - source row
    // sc - source column
    // dr - destination row
    // dc - destination column
    public static ArrayList<String> getMazePaths(int sr, int sc, int dr, int dc) {

        if (sr>dr || sc>dc){
            return new ArrayList<String>();
        }
        else if (sr == dr && dc == sc){
            ArrayList<String> st = new ArrayList<String>();
            st.add("");
            return st;
        }

        ArrayList<String> horizontalPath = getMazePaths(sr  ,sc+1,dr,dc);
        ArrayList<String>   verticalPath = getMazePaths(sr+1,  sc,dr,dc);

        ArrayList<String> result = new ArrayList<String>();

        for (String i : horizontalPath){
            result.add('h' + i);
        }
        
        for (String i : verticalPath){
            result.add('v' + i);
        }
        // System.out.println(horizontalPath + " " + verticalPath);
        // System.out.println(result+ "   "+sr+sc);
        return result;
    }

}
