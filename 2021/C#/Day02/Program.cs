
using System;
using System.IO;

class Program {

    static void Main(string[] args) {

        List<string> data = BuglLib.Files.ReadFile(args[0]);

        Solve1(data);

        Solve2(data);

    }

    static void Solve1(List<string> data) {

        int pos = 0;
        int depth = 0;

        foreach (string s in data) {
            
            string[] dirX = s.Split(" ");

            switch (dirX[0]) {
                case "forward":
                    pos += int.Parse(dirX[1]);
                    break;
                case "down":
                    depth += int.Parse(dirX[1]);
                    break;
                case "up":
                    depth -= int.Parse(dirX[1]);
                    break;
            }

        }

        Console.WriteLine(String.Format("Part One | Position: {0} | Depth: {1} | Result: {2}", pos, depth, pos * depth));

    }

    static void Solve2(List<string> data) {

        int pos = 0;
        int depth = 0;
        int aim = 0;

        foreach (string s in data) {
            
            string[] dirX = s.Split(" ");

            switch (dirX[0]) {
                case "forward":
                    pos += int.Parse(dirX[1]);
                    depth += (aim * int.Parse(dirX[1]));
                    break;
                case "down":
                    aim += int.Parse(dirX[1]);
                    break;
                case "up":
                    aim -= int.Parse(dirX[1]);
                    break;
            }

        }

        Console.WriteLine(String.Format("Part Two | Position: {0} | Depth: {1} | Result: {2}", pos, depth, pos * depth));

    }

}
