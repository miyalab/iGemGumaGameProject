
namespace ImageFlipHorizontal
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
            this.buttonConverter = new System.Windows.Forms.Button();
            this.textBoxLog = new System.Windows.Forms.TextBox();
            this.SuspendLayout();
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
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle;
            this.Name = "FormMain";
            this.Text = "左右変換";
            this.DragDrop += new System.Windows.Forms.DragEventHandler(this.FormMain_DragDrop);
            this.DragEnter += new System.Windows.Forms.DragEventHandler(this.FormMain_DragEnter);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion
        private System.Windows.Forms.Button buttonConverter;
        private System.Windows.Forms.TextBox textBoxLog;
    }
}

