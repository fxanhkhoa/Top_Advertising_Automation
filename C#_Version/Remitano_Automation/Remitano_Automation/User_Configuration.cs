using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;

namespace Remitano_Automation
{
    class User_Configuration
    {
        public int delayEachPage { get; set; }
        public int delayEachPost { get; set; }
        public float maxBTC { get; set; }
        public int pageFrom { get; set; }
        public int pageTo { get; set; }
        public string linkLogIn { get; set; }
        public string accountNumber { get; set; }
        public string accountName { get; set; }
        public string bankName { get; set; }
        public float bitToSell { get; set; }
        public float multiply { get; set; }

        public void save()
        {
            string jsonData = JsonConvert.SerializeObject(this);
            string path = "config.txt";
            using (StreamWriter sw = File.AppendText(path)) { }

            using (StreamWriter writetext = new StreamWriter(path))
            {
                writetext.Write(jsonData);
            }
        }

        public User_Configuration load()
        {
            try
            {
                string path = "config.txt";
                using (StreamReader readtext = new StreamReader(path))
                {
                    string jsonData = readtext.ReadLine();
                    Console.WriteLine(jsonData);
                    User_Configuration cfg = JsonConvert.DeserializeObject<User_Configuration>(jsonData);
                    return cfg;
                }
            }
            catch (Exception e)
            {
                return null;
            }
        }
    }
}
