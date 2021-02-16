import java.util.ArrayList;

class Main {
  public ArrayList<Integer> win(int n, int lb, int ub) {
    if (n > 2*(ub-lb)+1)
      return null;
    ArrayList<Integer> seq = new ArrayList<Integer>();
    if (ub-lb+1 >= n-1) {
      seq.add(ub-1);
      n--;
    } else {
      for (int i = n-(ub-lb)-1; i > 0; i--) {
        seq.add(ub-i);
	n--;
      }
    }
    int i = 0;
    while (n-- > 0) {
      seq.add(ub-(i++));
    }
    return seq;
  }

  public static void main(String[] args) {
    System.out.println("Hello world!");
    int n = 16;
    int lb = 1;
    int ub = 12;
    Main m = new Main();
    System.out.println(m.win(n, lb, ub));
  }
}

