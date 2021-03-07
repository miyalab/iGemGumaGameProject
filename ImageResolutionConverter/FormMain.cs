using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace ImageResolutionConverter
{
    public partial class FormMain : Form
    {
        readonly string[] imgExt =
        {
            "png",
            "PNG",
            "jpg",
            "JPG",
            "bmp",
            "BMP"
        };

        private List<string> convertFileList;

        /// <summary>
        /// メインフォーム コンストラクタ
        /// </summary>
        public FormMain()
        {
            // フォーム初期化
            InitializeComponent();

            // インスタンス初期化
            convertFileList = new List<string>();
        }

        /// <summary>
        /// ドラッグドロップ時処理
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void FormMain_DragDrop(object sender, DragEventArgs e)
        {
            // ドロップファイルのパスリスト
            string[] files = (string[])e.Data.GetData(DataFormats.FileDrop, false);
            
            textBoxLog.Clear();
            convertFileList.Clear();
            textBoxLog.AppendText("ドロップファイル");
            foreach(string file in files)
            {
                textBoxLog.AppendText(file + Environment.NewLine);

                // 拡張子チェック
                string[] ext = file.Split('.');
                foreach(string check in imgExt)
                {
                    if (ext[ext.Count() - 1] == check)
                    {
                        convertFileList.Add(file);
                        break;
                    }
                }
                
            }
        }

        /// <summary>
        /// メインフォームでのドラッグ時処理
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void FormMain_DragEnter(object sender, DragEventArgs e)
        {
            if (e.Data.GetDataPresent(DataFormats.FileDrop))
            {
                e.Effect = DragDropEffects.All;
            }
            else
            {
                e.Effect = DragDropEffects.None;
            }
        }

        /// <summary>
        /// 「開く」ボタンクリック時処理
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void buttonFileOpen_Click(object sender, EventArgs e)
        {

        }

        /// <summary>
        /// 「変換」ボタンクリック時処理
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void buttonConverter_Click(object sender, EventArgs e)
        {
            int ConvertWidth = (int)numericUpDownResHorizontal.Value;
            int ConvertHeight = (int)numericUpDownResVertical.Value;

            textBoxLog.AppendText("変換ファイル" + Environment.NewLine);
            foreach(string file in convertFileList)
            {
                textBoxLog.AppendText(file + Environment.NewLine);

                string dir = "";
                string[] split = file.Split('\\');
                for (int i=0; i<split.Length - 1; i++)
                {
                    dir += split[i];
                    dir += "\\";
                }

                // フォルダ作成
                if (!Directory.Exists(dir + "Converter"))
                {
                    Directory.CreateDirectory(dir + "Converter");
                }

                // 解像度を指定して読み込み
                Bitmap bmp = new Bitmap(Image.FromFile(file), new Size(ConvertWidth, ConvertHeight));
                bmp.Save(dir + "Converter\\" + split[split.Length - 1], System.Drawing.Imaging.ImageFormat.Png);
                
            }
        }
    }
}
