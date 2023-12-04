using System;
using System.IO;

namespace BuglLib {

    class Files {

        public static List<string> ReadFile(string path) {

            List<string> data = new List<string>();

            using (StreamReader sr = File.OpenText(path)) {

                string? s;

                while ((s = sr.ReadLine()) != null) {

                    data.Add(s);

                }

            }

            return data;

        }

    }

}