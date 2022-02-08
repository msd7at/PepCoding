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

       ArrayList<String> result = new ArrayList();


        for (int q=1; q<=dc-sc;q++ ){

        ArrayList<String> horizontalPath = getMazePaths(sr  ,sc+q,dr,dc);
          for (String i : horizontalPath){
            result.add("h"+q+i);
        }

        }


        for (int q=1; q<=dr-sr;q++ ){

        ArrayList<String>   verticalPath = getMazePaths(sr+q,  sc,dr,dc);
        for (String i : verticalPath){
            result.add("v"+q+i);
        }

        }

 
        for (int q=1; q<=dc-sc;q++ ){

       ArrayList<String>   dPath = getMazePaths(sr+q, q+sc,dr,dc);
        for (String i : dPath){
            result.add("d"+q+i);
        }

        }

 
            

  

        return result;
    }

}
