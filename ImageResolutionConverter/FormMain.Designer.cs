
namespace ImageResolutionConverter
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
            this.buttonFileOpen = new System.Windows.Forms.Button();
            this.buttonConverter = new System.Windows.Forms.Button();
            this.textBoxLog = new System.Windows.Forms.TextBox();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDownResHorizontal)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDownResVertical)).BeginInit();
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
            64,
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
            64,
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
            // buttonFileOpen
            // 
            this.buttonFileOpen.Location = new System.Drawing.Point(313, 12);
            this.buttonFileOpen.Name = "buttonFileOpen";
            this.buttonFileOpen.Size = new System.Drawing.Size(75, 23);
            this.buttonFileOpen.TabIndex = 4;
            this.buttonFileOpen.Text = "開く";
            this.buttonFileOpen.UseVisualStyleBackColor = true;
            this.buttonFileOpen.Click += new System.EventHandler(this.buttonFileOpen_Click);
            // 
            // buttonConverter
            // 
            this.buttonConverter.Location = new System.Drawing.Point(394, 12);
            this.buttonConverter.Name = "buttonConverter";
            this.buttonConverter.Size = new System.Drawing.Size(75, 23);
            this.buttonConverter.TabIndex = 5;
            this.buttonConverter.Text = "変換";
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
            // FormMain
            // 
            this.AllowDrop = true;
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(480, 450);
            this.Controls.Add(this.textBoxLog);
            this.Controls.Add(this.buttonConverter);
            this.Controls.Add(this.buttonFileOpen);
            this.Controls.Add(this.labelRes);
            this.Controls.Add(this.labelTimes);
            this.Controls.Add(this.numericUpDownResVertical);
            this.Controls.Add(this.numericUpDownResHorizontal);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle;
            this.Name = "FormMain";
            this.Text = "解像度変換";
            this.DragDrop += new System.Windows.Forms.DragEventHandler(this.FormMain_DragDrop);
            this.DragEnter += new System.Windows.Forms.DragEventHandler(this.FormMain_DragEnter);
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDownResHorizontal)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDownResVertical)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.NumericUpDown numericUpDownResHorizontal;
        private System.Windows.Forms.NumericUpDown numericUpDownResVertical;
        private System.Windows.Forms.Label labelTimes;
        private System.Windows.Forms.Label labelRes;
        private System.Windows.Forms.Button buttonFileOpen;
        private System.Windows.Forms.Button buttonConverter;
        private System.Windows.Forms.TextBox textBoxLog;
    }
}

