using System;
using System.IO;
using System.Collections.Generic;

using BuglLib;

class Program {

    static void Main(string[] args) {

        List<string> data = BuglLib.Files.ReadFile(args[0]);

        int[] values = new int[data.Count];

        for (int i = 0; i < data.Count; i++) {

            values[i] = int.Parse(data[i]);

        }

        Console.WriteLine(SolveFirst(values));

        Console.WriteLine(SolveSecond(values));

    }

    static int SolveFirst(int[] input) {

        int count = 0;

        for (int i = 0; i < input.Length - 1; i++) {

            if (input[i] < input[i + 1]) {
                count++;
            }

        }

        return count;

    }

    static int SolveSecond(int[] input) {

        int[] sums = new int[input.Length - 2];

        for (int i = 0; i < input.Length - 2; i++) {

            sums[i] = input[i] + input[i + 1] + input[i + 2];

        }

        return SolveFirst(sums);

    }

}
