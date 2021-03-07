
namespace ImageOverlap
{
    partial class FormMain
    {
        /// <summary>
        /// 必要なデザイナー変数です。
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 使用中のリソースをすべてクリーンアップします。
        /// </summary>
        /// <param name="disposing">マネージド リソースを破棄する場合は true を指定し、その他の場合は false を指定します。</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows フォーム デザイナーで生成されたコード

        /// <summary>
        /// デザイナー サポートに必要なメソッドです。このメソッドの内容を
        /// コード エディターで変更しないでください。
        /// </summary>
        private void InitializeComponent()
        {
            this.numericUpDownResHorizontal = new System.Windows.Forms.NumericUpDown();
            this.numericUpDownResVertical = new System.Windows.Forms.NumericUpDown();
            this.labelTimes = new System.Windows.Forms.Label();
            this.labelRes = new System.Windows.Forms.Label();
            this.buttonFileClear = new System.Windows.Forms.Button();
            this.buttonConverter = new System.Windows.Forms.Button();
            this.textBoxLog = new System.Windows.Forms.TextBox();
            this.buttonPaste = new System.Windows.Forms.Button();
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.pictureBox2 = new System.Windows.Forms.PictureBox();
            this.pictureBox3 = new System.Windows.Forms.PictureBox();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDownResHorizontal)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDownResVertical)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox2)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox3)).BeginInit();
            this.SuspendLayout();
            // 
            // numericUpDownResHorizontal
            // 
            this.numericUpDownResHorizontal.Location = new System.Drawing.Point(271, 41);
            this.numericUpDownResHorizontal.Maximum = new decimal(new int[] {
            1920,
            0,
            0,
            0});
            this.numericUpDownResHorizontal.Name = "numericUpDownResHorizontal";
            this.numericUpDownResHorizontal.Size = new System.Drawing.Size(86, 19);
            this.numericUpDownResHorizontal.TabIndex = 0;
            this.numericUpDownResHorizontal.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            this.numericUpDownResHorizontal.Value = new decimal(new int[] {
            32,
            0,
            0,
            0});
            // 
            // numericUpDownResVertical
            // 
            this.numericUpDownResVertical.Location = new System.Drawing.Point(383, 41);
            this.numericUpDownResVertical.Maximum = new decimal(new int[] {
            1920,
            0,
            0,
            0});
            this.numericUpDownResVertical.Name = "numericUpDownResVertical";
            this.numericUpDownResVertical.Size = new System.Drawing.Size(86, 19);
            this.numericUpDownResVertical.TabIndex = 1;
            this.numericUpDownResVertical.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            this.numericUpDownResVertical.Value = new decimal(new int[] {
            32,
            0,
            0,
            0});
            // 
            // labelTimes
            // 
            this.labelTimes.AutoSize = true;
            this.labelTimes.Font = new System.Drawing.Font("Microsoft Sans Serif", 9F);
            this.labelTimes.Location = new System.Drawing.Point(363, 43);
            this.labelTimes.Name = "labelTimes";
            this.labelTimes.Size = new System.Drawing.Size(15, 15);
            this.labelTimes.TabIndex = 2;
            this.labelTimes.Text = "X";
            // 
            // labelRes
            // 
            this.labelRes.AutoSize = true;
            this.labelRes.Location = new System.Drawing.Point(224, 45);
            this.labelRes.Name = "labelRes";
            this.labelRes.Size = new System.Drawing.Size(41, 12);
            this.labelRes.TabIndex = 3;
            this.labelRes.Text = "解像度";
            // 
            // buttonFileClear
            // 
            this.buttonFileClear.Location = new System.Drawing.Point(313, 12);
            this.buttonFileClear.Name = "buttonFileClear";
            this.buttonFileClear.Size = new System.Drawing.Size(75, 23);
            this.buttonFileClear.TabIndex = 4;
            this.buttonFileClear.Text = "クリア";
            this.buttonFileClear.UseVisualStyleBackColor = true;
            this.buttonFileClear.Click += new System.EventHandler(this.buttonFileClear_Click);
            // 
            // buttonConverter
            // 
            this.buttonConverter.Location = new System.Drawing.Point(394, 12);
            this.buttonConverter.Name = "buttonConverter";
            this.buttonConverter.Size = new System.Drawing.Size(75, 23);
            this.buttonConverter.TabIndex = 5;
            this.buttonConverter.Text = "保存";
            this.buttonConverter.UseVisualStyleBackColor = true;
            this.buttonConverter.Click += new System.EventHandler(this.buttonConverter_Click);
            // 
            // textBoxLog
            // 
            this.textBoxLog.Location = new System.Drawing.Point(12, 66);
            this.textBoxLog.Multiline = true;
            this.textBoxLog.Name = "textBoxLog";
            this.textBoxLog.ScrollBars = System.Windows.Forms.ScrollBars.Vertical;
            this.textBoxLog.Size = new System.Drawing.Size(457, 372);
            this.textBoxLog.TabIndex = 6;
            // 
            // buttonPaste
            // 
            this.buttonPaste.Location = new System.Drawing.Point(232, 12);
            this.buttonPaste.Name = "buttonPaste";
            this.buttonPaste.Size = new System.Drawing.Size(75, 23);
            this.buttonPaste.TabIndex = 7;
            this.buttonPaste.Text = "貼り付け";
            this.buttonPaste.UseVisualStyleBackColor = true;
            this.buttonPaste.Click += new System.EventHandler(this.buttonPaste_Click);
            // 
            // pictureBox1
            // 
            this.pictureBox1.Location = new System.Drawing.Point(12, 444);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(143, 107);
            this.pictureBox1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.AutoSize;
            this.pictureBox1.TabIndex = 8;
            this.pictureBox1.TabStop = false;
            // 
            // pictureBox2
            // 
            this.pictureBox2.Location = new System.Drawing.Point(161, 444);
            this.pictureBox2.Name = "pictureBox2";
            this.pictureBox2.Size = new System.Drawing.Size(143, 107);
            this.pictureBox2.SizeMode = System.Windows.Forms.PictureBoxSizeMode.AutoSize;
            this.pictureBox2.TabIndex = 9;
            this.pictureBox2.TabStop = false;
            // 
            // pictureBox3
            // 
            this.pictureBox3.Location = new System.Drawing.Point(310, 444);
            this.pictureBox3.Name = "pictureBox3";
            this.pictureBox3.Size = new System.Drawing.Size(143, 107);
            this.pictureBox3.SizeMode = System.Windows.Forms.PictureBoxSizeMode.AutoSize;
            this.pictureBox3.TabIndex = 10;
            this.pictureBox3.TabStop = false;
            // 
            // FormMain
            // 
            this.AllowDrop = true;
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(480, 563);
            this.Controls.Add(this.pictureBox3);
            this.Controls.Add(this.pictureBox2);
            this.Controls.Add(this.pictureBox1);
            this.Controls.Add(this.buttonPaste);
            this.Controls.Add(this.textBoxLog);
            this.Controls.Add(this.buttonConverter);
            this.Controls.Add(this.buttonFileClear);
            this.Controls.Add(this.labelRes);
            this.Controls.Add(this.labelTimes);
            this.Controls.Add(this.numericUpDownResVertical);
            this.Controls.Add(this.numericUpDownResHorizontal);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle;
            this.Name = "FormMain";
            this.Text = "画像合成";
            this.DragDrop += new System.Windows.Forms.DragEventHandler(this.FormMain_DragDrop);
            this.DragEnter += new System.Windows.Forms.DragEventHandler(this.FormMain_DragEnter);
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDownResHorizontal)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDownResVertical)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox2)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox3)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.NumericUpDown numericUpDownResHorizontal;
        private System.Windows.Forms.NumericUpDown numericUpDownResVertical;
        private System.Windows.Forms.Label labelTimes;
        private System.Windows.Forms.Label labelRes;
        private System.Windows.Forms.Button buttonFileClear;
        private System.Windows.Forms.Button buttonConverter;
        private System.Windows.Forms.TextBox textBoxLog;
        private System.Windows.Forms.Button buttonPaste;
        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.PictureBox pictureBox2;
        private System.Windows.Forms.PictureBox pictureBox3;
    }
}

