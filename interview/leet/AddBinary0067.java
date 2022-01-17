package com.company;

public class AddBinary0067 {
    public String addBinary(String a, String b) {
        int al = a.length(), bl = b.length();
        int l = Math.max(al, bl);
        int sum, cin = 0, ai, bi;
        String ret = "";
        for (int i = 0; i < l; i++) {
            ai = (i >= al) ? 0 : Integer.parseInt(String.valueOf(a.charAt(al-i-1)));
            bi = (i >= bl) ? 0 : Integer.parseInt(String.valueOf(b.charAt(bl-i-1)));
            sum = (ai + bi + cin) % 2;
            cin = ((ai + bi + cin) >= 2) ? 1 : 0;
            ret = String.valueOf(sum).concat(ret);
        }
        if (cin > 0) ret = String.valueOf(cin).concat(ret);
        return ret;
    }

    public static void main(String[] args) {
        AddBinary0067 solution = new AddBinary0067();
        System.out.println(solution.addBinary("11", "1"));
        System.out.println(solution.addBinary("1010", "1011"));
        System.out.println(solution.addBinary("0", "0"));
        System.out.println(solution.addBinary("0", "1"));
    }
}
