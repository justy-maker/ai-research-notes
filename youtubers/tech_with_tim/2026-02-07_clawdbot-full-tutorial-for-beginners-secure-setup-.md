---
video_id: tnsrnsy_Lus
title: "ClawdBot Full Tutorial for Beginners: SECURE Setup Guide"
date: 2026-02-07
channel: Tech With Tim
url: https://www.youtube.com/watch?v=tnsrnsy_Lus
---

# ClawdBot 安全設置完整教學：新手指南

本影片提供一份完整且安全的 ClawdBot (或 OpenClaw) 設定指南。強調安全性，保護你的資料、憑證和整體安全。許多現有教學存在嚴重的安全漏洞，可能導致駭客入侵、竊取 API 金鑰、控制你的電腦甚至存取銀行帳戶等。本教學雖然較長且複雜，但會教你安全設定的原因，確保長期使用的安全性。

## 重點摘要

*   **不要在本地電腦運行：** 避免將 ClawdBot 運行在你的主要作業系統或任何實體硬體設備上。
*   **使用虛擬私人伺服器 (VPS)：** VPS 比本地伺服器更安全，且價格更低廉。
*   **建立 VPN 通道：** 使用 VPN (Virtual Private Network) 隧道建立安全的互動方法，防止未授權的存取。
*   **IP 層級限制：** 限制只有授權的設備才能與你的 ClawdBot 通訊。
*   **防範 Prompt Injection 攻擊：** 避免他人透過惡意 Prompt 控制你的模型。

## 詳細內容

### 什麼是 OpenClaw (ClawdBot)?

OpenClaw 本身並非 AI，而是一個開源軟體，它是一個複雜的訊息佇列或協調層，架構在 AI 模型之上。它協調訊息到大型語言模型 (LLM)，使其能夠在後台執行任務。你需要小心輸入和輸出資料，因為它只是訊息傳遞系統。

### 安全考量

連接的工具和服務越多（如 Google Drive、Gmail、API 金鑰），風險就越高。目前的 ClawdBot 設定方式普遍不安全。

### 伺服器設置

1.  **選擇 VPS：** 推薦使用 Hostinger，它提供價格實惠的 VPS，並與本教學相容。可以使用提供的連結和優惠碼 (tech with Tim) 獲得折扣。建議選擇 KVM2 方案。
2.  **作業系統：** 選擇 Debian 13 作為作業系統。
3.  **Root 密碼：** 設置一個強大的隨機 Root 密碼。
4.  **SSH 連線：** 使用 SSH (Secure Shell) 連線到伺服器。
5.  **Tailscale VPN 設定：**
    *   安裝 Tailscale，建立一個虛擬私人網路，僅允許授權設備連線。
    *   使用 `curl -fsl https://tailscale.com/install.sh | sh` 命令安裝 Tailscale。
    *   使用 `tailscale up --ssh` 命令啟動 Tailscale SSH 服務。
    *   在瀏覽器中驗證 Tailscale 帳戶。
    *   在本地電腦下載並安裝 Tailscale。
    *   登入 Tailscale 並連接到虛擬私人網路。
6.  **禁用 Root 登入並建立新使用者：**
    *   編輯 SSH 設定檔 (`nano /etc/ssh/sshd_config`)。
    *   修改 `ListenAddress` 為 Tailscale IP。
    *   設定 `PasswordAuthentication no`。
    *   設定 `PermitRootLogin no`。
    *   儲存檔案 (Ctrl+S) 並關閉 (Ctrl+X)。
    *   建立新使用者：`adduser [username]`。
    *   將使用者新增至 sudo 群組：`usermod -aG sudo [username]`。
    *   切換至新使用者：`su [username]`。
    *   測試 sudo 權限：`sudo whoami` (應顯示 root)。
    *   重新啟動 SSH 服務：`systemctl restart ssh`。
7.  **安裝 OpenClaw：** 從 OpenClaw 網站複製 Linux 安裝指令並執行。
8.  **OpenClaw 設定：** 依照指示操作。選擇手動設定，並配置 AI 模型 (OpenAI 或 Anthropic)。使用 API 金鑰或現有的訂閱服務。

## 結論與心得

本教學提供了一個安全設定 ClawdBot 的詳盡指南。雖然步驟較多，但能有效避免潛在的安全風險。使用 VPS 和 VPN 等技術，能大幅提升系統的安全性。在設定過程中，務必仔細閱讀每個步驟的說明，確保正確操作。此外，建議定期更新軟體和系統，以應對新的安全威脅。


---
*摘要由 AI 自動生成，內容僅供參考*
