

package POMSystem;

import POMSystem.Class.Admin;
import POMSystem.Class.FileHandling;
import POMSystem.Class.FileSerialization;
import POMSystem.Class.User;
import POMSystem.Page.SupplierItemUtility;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;


public class Trymethod2 {

    /*public static void firstrowregister(User user){
        FileSerialization fs=new FileSerialization();
        List<User> userList=new ArrayList<>();
        userList.add(user);
        if(fs.UserWrite(userList)){
            System.out.println(user+" have been Successful Register");
        }
        else{
            System.out.println("Something got error");
        }
    }
    public static void secondrowregister(User user){
        FileSerialization fs=new FileSerialization();
        List<User> userList=fs.UserRead();
        userList.add(user);
        if(fs.UserWrite(userList)){
            System.out.println(user+" have been Successful Register");
        }
        else{
            System.out.println("Something got error");
        }
    } 
    public static void main(String[] args) {
        Admin admin= new Admin("UserID","UserName","Password","Name","Contact","Email");
        firstrowregister(admin);
        Admin admin2= new Admin("Adm001","123","123","LIM ZHI SHEN","0121233211","ZhiShenLim@gmail.com");
        secondrowregister(admin2);
        List<String> save=new ArrayList<>();
        try(BufferedReader br=new BufferedReader(new FileReader("User for backup.txt"))){
            String lineString;
            while((lineString=br.readLine())!=null){
                save.add(lineString);
                
            }
        }
        catch(IOException Ex){
            System.out.println(Ex);
        }
        for (String i : save){
            String[] user =i.split(",");
            Admin admin1=new Admin(user[0],user[1],user[2],user[3],user[4],user[5]);
            secondrowregister(admin1);

    }        }*/

    

}
