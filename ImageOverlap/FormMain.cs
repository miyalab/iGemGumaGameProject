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

namespace ImageOverlap
{
    public partial class FormMain : Form
    {
        Graphics graphics;

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
            foreach (string file in files)
            {
                textBoxLog.AppendText(file + Environment.NewLine);

                // 拡張子チェック
                string[] ext = file.Split('.');
                foreach (string check in imgExt)
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
        /// 「変換」ボタンクリック時処理
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void buttonConverter_Click(object sender, EventArgs e)
        {
            if (pictureBox1.Image == null || pictureBox2.Image == null) return;

            Bitmap baseImage = new Bitmap(pictureBox1.Image);
            Bitmap logoImage = new Bitmap(pictureBox2.Image);
            Bitmap newImage = new Bitmap(baseImage);

            Graphics g = Graphics.FromImage(newImage);
            g.DrawImage(logoImage, 0, 0, logoImage.Width, logoImage.Height);

            g.Dispose();
            baseImage.Dispose();
            logoImage.Dispose();

            newImage.Save(convertFileList[0] + "-over.png", System.Drawing.Imaging.ImageFormat.Png);
            newImage.Dispose();

        }

        private void buttonFileClear_Click(object sender, EventArgs e)
        {
            convertFileList.Clear();
            textBoxLog.Clear();
            pictureBox2.Image = null;
            pictureBox1.Image = null;
            pictureBox3.Image = null;
        }

        private void buttonPaste_Click(object sender, EventArgs e)
        {
            graphics = pictureBox3.CreateGraphics();
            if (convertFileList.Count == 0) return;

            if (pictureBox1.Image == null)
            {
                pictureBox1.Image = System.Drawing.Image.FromFile(convertFileList[0]);

                graphics.DrawImage(pictureBox1.Image, 0, 0);
            }
            else if (pictureBox2.Image == null)
            {
                pictureBox2.Image = System.Drawing.Image.FromFile(convertFileList[0]);

                graphics.DrawImage(pictureBox2.Image, 0, 0);
            }

            //graphics.Dispose();
        }
    }
}
