import java.lang.*;
import java.util.ArrayList;
import java.util.Scanner;

class SignalProgram {
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        read_char("Enter a character : ");
    }

    // read_integer file
    public static int read_integer(String msg) {
        System.out.println(msg);
        String n = sc.next();
        if (isNumeric(n)) {
            return (n.charAt(0));
        } else {
            System.out.println("Ivalid Input!");
            return read_integer(msg);
        }
    }

    // read_integer file
    public static void read_char(String msg) {
        System.out.println(msg);
        char a = sc.next().charAt(0);
        System.out.println(((Object) a).getClass().getSimpleName());
    }

    public static boolean isNumeric(String n) {
        try {
            Integer.parseUnsignedInt(n);
            return true;
        } catch (NumberFormatException err) {
            return false;
        }
    }

    static int a;
    static ArrayList<Integer> ways = new ArrayList<Integer>();
    public static void stuff() {
        System.out.println("Enter the number of signals : ");
        int NoOfSignal = sc.nextInt();
        System.out.println("Does the signals have same time difference(y or n): ");
        char Sametime = sc.next().charAt(0);
        ArrayList<Integer> TimeToSig = new ArrayList<Integer>();
        if (Sametime == 'y' || Sametime == 'Y') {
            System.out.println("Enter time difference between each signals including last signal to destination : ");
            int SigToDest = sc.nextInt();
            for (int i = 0; i < NoOfSignal + 1; i++) {
                TimeToSig.add(SigToDest);
            }
        } else {
            for (int i = 0; i < NoOfSignal; i++) {
                System.out.println("Enter time to signal : ");
                int temp = sc.nextInt();
                TimeToSig.add(temp);
            }
            System.out.println("Enter time to reach destination from signal : ");
            char SigToDest = sc.next().charAt(0);
        }

        System.out.println("Does all signals are two ways (y or n) : ");
        char TwoWay = sc.next().charAt(0);

        ArrayList<Integer> paths = new ArrayList<Integer>();
        if (TwoWay == 'y' || TwoWay == 'Y') {
            for (int i = 0; i < NoOfSignal + 1; i++) {
                paths.add(2);
            }
        } else {
            for (int i = 0; i < NoOfSignal; i++) {
                System.out.println("Enter number of paths at signal (2-4) : ");
                int temp = sc.nextInt();
                paths.add(temp);
            }
        }
        System.out.println("Enter the signal time : ");
        int signal = sc.nextInt();

        // Generating the ways
        for (int i = 0; i < signal + 1; i++) {
            ways.add(i);
        }
        int two = 2 * signal;
        int three = 3 * signal;
        int four = 4 * signal;
        for (int i = 0; i < paths.size(); i++) {
            if (paths.indexOf(i) == 2) {
                a = two;
            } else if (paths.indexOf(i) == 3) {
                a = three;
            } else {
                paths.set(i, four);
            }
        }
        for (int i = 0; i < NoOfSignal; i++) {
            for (int j = 0; j < ways.size(); j++) {
                int res = ways.indexOf(j) + a;
                ways.add(res);
            }
        }
    }

    // public static int issafe(ways, key){
    //     for (int i = 0; i < ways.size(); i++) {
    //         if()
    //     }
    // }
}
