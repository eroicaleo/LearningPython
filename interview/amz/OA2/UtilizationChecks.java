class Main {
  public int findInstance(int instances, int[] averageUtil) {
      int i = 0;
      int util, new_instances;
      while (i < averageUtil.length) {
          util = averageUtil[i];
	  new_instances = instances;
          if (util < 25) {
              new_instances = Math.max((int)Math.ceil(instances/2.0), 1);
          } else if (util > 60) {
              new_instances = instances*2 > 200000000 ? instances : instances*2;
          }
          i += (new_instances != instances ? 10 : 1);
	  instances = new_instances;
      }
      return instances;
  }
  public static void main(String[] args) {
    System.out.println("Hello world!");
    // int instances = 2;
    // int[] averageUtil = {25,23,1,2,3,4,5,6,7,8,9,10,76,80};
    int instances = 5;
    int[] averageUtil = {30,5,4,8,19,89};
    // int instances = 1;
    // int[] averageUtil = {5,10,80};
    Main m = new Main();
    System.out.println(m.findInstance(instances, averageUtil));
  }
}
