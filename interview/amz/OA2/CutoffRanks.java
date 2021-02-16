import java.util.Arrays;
import java.util.Collections;

class Main {
  public int cutoffRank(int cutoffRank, int num, Integer[] scores) {
    Arrays.sort(scores, Collections.reverseOrder());
    System.out.printf("Sorted scores: %s\n", Arrays.toString(scores));
    int currRank = 1;
    int i = 1;
    for (; i < scores.length; i++) {
      if (scores[i] < scores[i-1])
        currRank += (i-currRank+1);
      System.out.printf("scores: %d, rank: %d\n", scores[i], currRank);
      if (currRank > cutoffRank)
        break;
    }
    return (cutoffRank == 0) ? 0 : i;
  }

  public static void main(String[] args) {
    System.out.println("Hello world!");
    // int cutoffRank = 1;
    // int num = 4;
    // Integer[] scores = {25,100,50,50};
    int cutoffRank = 4;
    int num = 5;
    Integer[] scores = {2,2,3,4,5};
    Main m = new Main();
    System.out.println(m.cutoffRank(cutoffRank, num, scores));
  }
}

