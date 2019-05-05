using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using OpenQA.Selenium.Chrome;
using OpenQA.Selenium;
using OpenQA.Selenium.Remote;
using System.Threading;
using System.Collections.ObjectModel;
using OpenQA.Selenium.Interactions;
using OpenQA.Selenium.Support.UI;

namespace Remitano_Automation
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        /// <summary>
        /// Global variable
        /// </summary>
        User_Configuration cfg = new User_Configuration();
        BackgroundWorker processWorker;
        private ChromeDriverService service = ChromeDriverService.CreateDefaultService();
        private IWebDriver driver;
        public MainWindow()
        {
            InitializeComponent();

            processWorker = new BackgroundWorker();
            processWorker.WorkerSupportsCancellation = true;

            processWorker.DoWork += processWorkerDoWork;
        }

        private void processWorkerDoWork(object sender, DoWorkEventArgs e)
        {
            
            while (true)
            {
                // Clear Report
                report.Dispatcher.Invoke(new Action(() => report.Text = ""));

                /// Login ///
                driver.Navigate().GoToUrl(cfg.linkLogIn);
                Thread.Sleep(2000);

                /************ Sell Part ************/
                /// Get Price ///
                driver.Navigate().GoToUrl("https://remitano.com/btc/vn");
                Thread.Sleep(5000);

                // Try click VietNam //
                try
                {
                    String requiredXpath = "//i[contains(@class, 'fa icon-down-open-1')]";
                    driver.FindElement(By.XPath(requiredXpath)).Click();
                    Thread.Sleep(1000);

                    String value = "Việt Nam";
                    requiredXpath = "//span[text()=\'" + value + "\']";
                    driver.FindElement(By.XPath(requiredXpath)).Click();
                    Thread.Sleep(3000);

                    report.Dispatcher.Invoke(new Action(() => report.Text += "Đổi ngôn ngữ VN \n"));
                }
                catch (Exception ex)
                {
                    Console.WriteLine(ex);
                }

                //// Lấy giá từ trang ////
                ///
                List<double> price = new List<double>();
                List<double> limitBTC = new List<double>();

                for (int i = cfg.pageFrom; i <= cfg.pageTo; i++)
                {
                    ReadOnlyCollection<IWebElement> elements = driver.FindElements(By.ClassName("amount"));
                    ReadOnlyCollection<IWebElement> elements_tradelimit = driver.FindElements(By.ClassName("remi-offer-item-price-trade-limits"));

                    for (int j = 0; j < 5; j++)
                    {
                        double value = double.Parse(elements[j].GetAttribute("innerHTML").Replace(",", ""));
                        String max_value_str = elements_tradelimit[j].Text.Replace("Tối đa: ", "");
                        double max_value = double.Parse(max_value_str.Replace(" BTC", ""));
                        Console.WriteLine(value + " " + max_value);

                        if (max_value > cfg.maxBTC)
                        {
                            price.Add(value);
                        }
                    }
                    //string value_str = "Trang sau";
                    string value_str = (i + 1).ToString();
                    string requiredXpath = "//a[text()=\'" + value_str + "\']";
                    try
                    {
                        ((IJavaScriptExecutor)driver).ExecuteScript("window.scrollTo(200,0)");
                        driver.FindElement(By.XPath(requiredXpath)).Click();
                        report.Dispatcher.Invoke(new Action(() => report.Text += "Click trang sau \n"));
                    }
                    catch (Exception ex)
                    {
                        Console.WriteLine(ex);
                    }

                    Thread.Sleep(cfg.delayEachPage * 1000);
                }
                Console.WriteLine("Max: ", price.Max());
                report.Dispatcher.Invoke(new Action(() => report.Text += "Giá thấp nhất: " + price.Min().ToString() + "\n"));

                /************ Phần xóa *************/
                driver.Navigate().GoToUrl("https://remitano.com/btc/vn/dashboard/escrow/trades/active");
                Thread.Sleep(1000);

                // Try click VietNam //
                try
                {
                    string requiredXpath = "//i[contains(@class, 'fa icon-down-open-1')]";
                    driver.FindElement(By.XPath(requiredXpath)).Click();
                    Thread.Sleep(1000);

                    String value = "Việt Nam";
                    requiredXpath = "//span[text()=\'" + value + "\']";
                    driver.FindElement(By.XPath(requiredXpath)).Click();
                    Thread.Sleep(3000);

                    report.Dispatcher.Invoke(new Action(() => report.Text += "Đổi ngôn ngữ VN \n"));
                }
                catch (Exception ex)
                {
                    Console.WriteLine(ex);
                }

                try
                {
                    // Go to my Advertising board
                    string value = "Các quảng cáo của tôi";
                    string requiredXpath = "//span[text()=\'" + value + "\']";
                    driver.FindElement(By.XPath(requiredXpath)).Click();
                    report.Dispatcher.Invoke(new Action(() => report.Text += "Vào quảng cáo của tôi \n"));
                    Thread.Sleep(2000);

                    // Delete advertisement
                    value = "Xóa";
                    requiredXpath = "//span[text()=\'" + value + "\']";
                    driver.FindElement(By.XPath(requiredXpath)).Click();
                    report.Dispatcher.Invoke(new Action(() => report.Text += "Xóa quảng cáo \n"));
                    Thread.Sleep(2000);
                }
                catch (Exception ex)
                {
                    Console.WriteLine(ex);
                }
               


                ////// Wait for each post
                ///
                Thread.Sleep(cfg.delayEachPost * 1000);
            }
        }

        private void Window_Loaded(object sender, RoutedEventArgs e)
        {
            InitBankName();
            loadSetting();
        }










        ////////////// Initialize function ////////
        /// <summary>
        /// 
        /// </summary>
        /// 
        private void UpdateSettings()
        {
            try
            {
                cfg.delayEachPage = Convert.ToInt16(delayEachPage.Text);
                cfg.delayEachPost = Convert.ToInt16(delayEachPost.Text);
                cfg.maxBTC = float.Parse(maxBTC.Text);
                cfg.pageFrom = Convert.ToInt16(pageFrom.Text);
                cfg.pageTo = Convert.ToInt16(pageTo.Text);
                cfg.linkLogIn = linkLogIn.Text;
                cfg.accountNumber = accountNumber.Text;
                cfg.accountName = accountName.Text;
                cfg.bankName = bankName.Text;
                cfg.bitToSell = float.Parse(bitToSell.Text);
                cfg.multiply = float.Parse(multiply.Text);

                cfg.save();
            }
            catch (Exception e)
            {
                Console.WriteLine("Error writing app settings");
            }
        }
        private void loadSetting()
        {
            cfg = cfg.load();
            delayEachPage.Text = cfg.delayEachPage.ToString();
            delayEachPost.Text = cfg.delayEachPost.ToString();
            maxBTC.Text = cfg.maxBTC.ToString();
            pageFrom.Text = cfg.pageFrom.ToString();
            pageTo.Text = cfg.pageTo.ToString();
            linkLogIn.Text = cfg.linkLogIn;
            accountNumber.Text = cfg.accountNumber;
            accountName.Text = cfg.accountName;
            bankName.SelectedItem = cfg.bankName;
            bitToSell.Text = cfg.bitToSell.ToString();
            multiply.Text = cfg.multiply.ToString();
        }
        private void InitBankName()
        {
            bankName.Items.Add("ACB (Ngân hàng Á Châu)");
            bankName.Items.Add("Vietinbank");
            bankName.Items.Add("Agribank");
            bankName.Items.Add("Sacombank");
            bankName.Items.Add("NamABank");
            bankName.Items.Add("Vietcombank");
            bankName.Items.Add("Eximbank");
            bankName.Items.Add("BIDV");
            bankName.Items.Add("DongA Bank");
            bankName.Items.Add("Maritime Bank");
            bankName.Items.Add("Techcombank");
            bankName.Items.Add("VPBank");
            bankName.Items.Add("PVcom Bank");
            bankName.Items.Add("SHBank");
            bankName.Items.Add("HDBank");
            bankName.Items.Add("LienVietPostBank");
            bankName.Items.Add("TP Bank");
            bankName.Items.Add("SeABank");
            bankName.Items.Add("ABBank");
            bankName.Items.Add("BacABank");
            bankName.Items.Add("VIBBank");
            bankName.Items.Add("Thẻ ATM (Smartlink)");
            bankName.Items.Add("MB (Ngân hàng quân đội)");
            bankName.Items.Add("HSBC");
        }







        /// <summary>
        /// Event function
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>

        private void SaveSettingBTN_Click(object sender, RoutedEventArgs e)
        {
            UpdateSettings();
        }

        private void RunBTN_Click(object sender, RoutedEventArgs e)
        {
            UpdateSettings();
            service.Start();
            var options = new ChromeOptions();
            driver = new RemoteWebDriver(service.ServiceUrl, options);
            //driver.Manage().Window.Maximize();
            //////// Start processWorker///////
            ///

            processWorker.RunWorkerAsync();
        }
    }
}
