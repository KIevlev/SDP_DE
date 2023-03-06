package com.company;

import java.util.Random;
import org.apache.commons.lang3.time.StopWatch;
import java.util.stream.IntStream;

class Main {
    public static void main(String args[]) throws Exception {
        int[] test = {10, 7, 5, 8, 11};
/*        int[]  randomIntsArray = IntStream.generate(() -> new Random().nextInt(10000)).limit(540).toArray();
        StopWatch stopWatch = new StopWatch();
        stopWatch.start();
*/        // выполнение какой-то логики randomIntsArray
        System.out.println(get_max_profit(test));  // test -> randomIntsArray
/*         stopWatch.stop();
        System.out.println("Прошло времени, мс: " + stopWatch.getTime());

         StopWatch stopWatch1 = new StopWatch();
        stopWatch1.start();
        //
      System.out.println(get_max_profit2(randomIntsArray));
        stopWatch1.stop();
        System.out.println("Прошло времени, мс: " + stopWatch1.getTime());
*/
    }

    static int get_max_profit2(int[] stock_prices_yesterday)
    {
        int a = 0;
        if (stock_prices_yesterday == null || stock_prices_yesterday.length == 0)
            return -1;
        for (int i = 0; i < stock_prices_yesterday.length - 1; i++)
        {
            for (int j = i+1; j < stock_prices_yesterday.length; j++)
            {
                if (stock_prices_yesterday[j] - stock_prices_yesterday[i] > a)
                    a = stock_prices_yesterday[j] - stock_prices_yesterday[i];
            }
        } // сложность алгоритма N^2 (первый вариант, который пришёл в голову. Слишком затратный по времени)
        return a;
    }


    static int get_max_profit(int[] stock_prices_yesterday)
    {
        if (stock_prices_yesterday.length < 2)
            return -1;

        int min_price = stock_prices_yesterday[0];
        int max_profit = stock_prices_yesterday[1] - stock_prices_yesterday[0];

        for (int i = 1; i < stock_prices_yesterday.length; i++) {


            int potential_profit = stock_prices_yesterday[i] - min_price;

            max_profit = max_profit > potential_profit ? max_profit : potential_profit;

            min_price = min_price < stock_prices_yesterday[i] ? min_price : stock_prices_yesterday[i];
        }
        return max_profit;
    }
}

