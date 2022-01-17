package com.company;

import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;

public class CarPooling1094 {
    public boolean carPooling(int[][] trips, int capacity) {
        Arrays.sort(trips, Comparator.comparingInt((int[] a) -> a[1]));
        PriorityQueue<int []> heap = new PriorityQueue<>(Comparator.comparingInt((int[] a) -> -a[2]));
        int people = 0;
        for (int[] trip: trips) {
            // System.out.println(Arrays.toString(trip));
            while (heap.size() > 0 && heap.peek()[2] <= trip[1]) {
                people -= heap.poll()[0];
            }
            heap.offer(trip);
            people += trip[0];
            if (people > capacity)
                return false;
        }
        return true;
    }

    public static void main(String[] args) {
        CarPooling1094 cp = new CarPooling1094();
        int[][] trips = {{3, 3, 7}, {2, 1, 5}};
        System.out.println(cp.carPooling(trips, 4));
        System.out.println(cp.carPooling(trips, 5));
    }
}
