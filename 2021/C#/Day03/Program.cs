
using System;
using System.IO;

class Program {

    static void Main(string[] args) {

        List<string> data = BuglLib.Files.ReadFile(args[0]);

        int res1 = Solve1(data);
        int res2 = Solve2(data);

        Console.WriteLine(string.Format("Part One: {0}\nPart Two: {1}", res1, res2));

    }

    static int Solve1(List<string> data) {

        string gamma = "";
        string epsilon = "";

        int[] count = countOnes(data);

        foreach (int c in count) {
            
            if (c >= (data.Count / 2)) {
                gamma += "1";
                epsilon += "0";
            }
            else {
                gamma += "0";
                epsilon += "1";
            }

        }

        int gammaBin = binToDec(gamma);
        int epsilonBin = binToDec(epsilon);        

        return gammaBin * epsilonBin;

    }

    static int Solve2(List<string> data) {

        int oxy = Solve2Rec(data, countOnes(data), 0, '1');
        int co2 = Solve2Rec(data, countOnes(data), 0, '0');

        return oxy * co2;

    }

    static int Solve2Rec(List<string> list, int[] count, int currentIndex, char criteria) {

        if (list.Count == 1) {
            return binToDec(list[0]);
        }

        List<string> candidates = new List<string>();

        char inverseCriteria = (criteria == '1') ? '0' : '1';

        foreach (string s in list) {

            if (count[currentIndex] >= (list.Count / 2)) {

                if (s[currentIndex] == criteria) {
                    candidates.Add(s);
                }

            }
            else {

                if (s[currentIndex] == inverseCriteria) {
                    candidates.Add(s);
                }

            }

        }

        int[] newCount = countOnes(candidates);

        return Solve2Rec(candidates, newCount, currentIndex + 1, criteria);

    }

    static int[] countOnes(List<string> list) {

        int[] count = new int[list[0].Length];

        for (int i = 0; i < list.Count; i++) {
            for (int j = 0; j < list[i].Length; j++) {

                if (list[i][j] == '1') {
                    count[j]++;
                }

            }
        }

        return count;

    }

    static int binToDec(string s) {

        int n = 0;

        for (int i = 0; i < s.Length; i++) {

            char c = s[i];

            int exp = s.Length - 1 - i;

            if (c == '1') {
                n += (int) Math.Pow(2, exp);
            }

        }

        return n;

    }

}