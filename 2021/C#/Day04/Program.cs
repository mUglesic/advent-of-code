
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

        (int[] drawnNums, List<BingoBoard> boards) = ParseData(data);

        foreach (int num in drawnNums) {

            foreach (BingoBoard board in boards) {

                board.Mark(num);

                if (board.Won()) {

                    return board.Sum() * num;

                }

            }

        }

        return -1;

    }

    static int Solve2(List<string> data) {

        (int[] drawnNums, List<BingoBoard> boards) = ParseData(data);

        int[] count = new int[boards.Count];

        for (int bi = 0; bi < boards.Count; bi++) {

            BingoBoard board = boards[bi];

            for (int i = 0; i < drawnNums.Length; i++) {

                board.Mark(drawnNums[i]);

                if (board.Won()) {

                    count[bi] = i;
                    
                    break;

                }

            }

        }

        (int value, int index) = count.Select((v, i) => (v, i)).Max();

        return boards[index].Sum() * drawnNums[value];

    }

    static (int[], List<BingoBoard>) ParseData(List<string> data) {

        int[] drawnNums = Array.ConvertAll(data[0].Split(","), int.Parse);

        List<BingoBoard> boards = new List<BingoBoard>();

        BingoBoard current = new BingoBoard(5, 5);

        boards.Add(current);

        for (int i = 2; i < data.Count; i++) {

            if (data[i] == "") {

                current = new BingoBoard(5, 5);

                boards.Add(current);

            }
            else {

                string[] line = data[i].Split(new char[0], StringSplitOptions.RemoveEmptyEntries);

                for (int j = 0; j < line.Length; j++) {
                    current.SetNum(int.Parse(line[j]), (i - 2) % 6, j);
                }

            }

        }

        return (drawnNums, boards);

    }

    public static bool All(bool[] arr, bool n) {

        bool allSame = true;

        foreach (bool a in arr) {
            if (a != n) {
                allSame = false;
            }
        }

        return allSame;

    }

}

class BingoBoard {

    private int[][] board;
    private bool[][] marked;

    public BingoBoard(int n, int m) {

        this.board = new int[n][];

        this.marked = new bool[n][];

        this.InitArrays(m);

    }

    private void InitArrays(int m) {

        for (int i = 0; i < this.board.Length; i++) this.board[i] = new int[m];
        for (int i = 0; i < this.marked.Length; i++) this.marked[i] = new bool[m];

    }

    public void SetNum(int n, int i, int j) {

        this.board[i][j] = n;

    }

    public void Mark(int n) {

        for (int i = 0; i < this.marked.Length; i++) {
            for (int j = 0; j < this.marked[i].Length; j++) {

                if (this.board[i][j] == n) {
                    this.marked[i][j] = true;
                }

            }
        }

    }

    public int Sum() {

        int sum = 0;

        for (int i = 0; i < this.board.Length; i++) {
            for (int j = 0; j < this.board[i].Length; j++) {

                if (!this.marked[i][j]) {
                    sum += this.board[i][j];
                }

            }
        }

        return sum;

    }

    public bool Won() {

        foreach (bool[] line in this.marked) {

            if (Program.All(line, true)) {
                return true;
            }

        }

        for (int i = 0; i < this.board.Length; i++) {

            bool[] temp = new bool[this.board[i].Length];

            for (int j = 0; j < this.marked[i].Length; j++) {

                temp[j] = this.marked[j][i];

            }

            if (Program.All(temp, true)) {
                return true;
            }

        }

        return false;

    }

    public override string ToString() {

        string s = "";

        foreach (int[] line in this.board) {
            foreach (int element in line) {

                s += string.Format("{0,2} ", element);

            }

            s += "\n";

        }

        return s;

    }


}