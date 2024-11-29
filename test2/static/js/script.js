// 模拟加载模型的函数
function loadModel() {
    const chatBox = document.getElementById("chat-box");
    const botMessage = document.createElement("p");
    botMessage.classList.add("bot-message");
    botMessage.textContent = "模型已加载！现在可以开始对话。";
    chatBox.appendChild(botMessage);
    chatBox.scrollTop = chatBox.scrollHeight;
}

// 模拟卸载模型的函数
function unloadModel() {
    const chatBox = document.getElementById("chat-box");
    const botMessage = document.createElement("p");
    botMessage.classList.add("bot-message");
    botMessage.textContent = "模型已卸载！无法继续对话。";
    chatBox.appendChild(botMessage);
    chatBox.scrollTop = chatBox.scrollHeight;
}

// 清除对话框内容的函数
function clearChat() {
    const chatBox = document.getElementById("chat-box");
    chatBox.innerHTML = "";  // 清空对话框内容
}

// 发送消息函数
function sendMessage() {
    const userInput = document.getElementById("user-input").value;
    if (userInput.trim() === "") return;

    // 显示用户的消息
    const chatBox = document.getElementById("chat-box");
    const userMessage = document.createElement("p");
    userMessage.classList.add("user-message");
    userMessage.textContent = userInput;
    chatBox.appendChild(userMessage);

    // 清空输入框
    document.getElementById("user-input").value = "";

    // 生成机器人回复（可以根据实际情况修改）
    const botResponse = generateBotResponse(userInput);

    // 等待短暂延迟后显示机器人的回复
    setTimeout(() => {
        const botMessage = document.createElement("p");
        botMessage.classList.add("bot-message");
        botMessage.textContent = botResponse;
        chatBox.appendChild(botMessage);

        // 滚动到最新的消息
        chatBox.scrollTop = chatBox.scrollHeight;
    }, 500);
}

// 检测按下的键是否是Enter键
function checkEnter(event) {
    if (event.key === "Enter") {
        sendMessage();
    }
}

// 模拟机器人回复的函数
function generateBotResponse(input) {
    if (input.includes("你好")) {
        return "你好呀！有什么可以帮忙的吗？";
    } else if (input.includes("天气")) {
        return "今天天气不错，适合外出活动！";
    } else {
        return "我还在学习中，暂时不太理解这个问题。";
    }
}

// 显示功能待开发的消息
function showFeatureMessage(feature) {
    const chatBox = document.getElementById("chat-box");
    const botMessage = document.createElement("p");
    botMessage.classList.add("bot-message");
    botMessage.textContent = `${feature} 功能待开发。`;
    chatBox.appendChild(botMessage);
    chatBox.scrollTop = chatBox.scrollHeight;
}

// 显示文件路径输入框
function showFileInput() {
    const fileInputContainer = document.getElementById("file-input-container");
    fileInputContainer.style.display = "block";
}

function loadFile() {
    const filePath = document.getElementById("file-path").value.trim();
    if (filePath === "") {
        alert("请输入文件路径");
        return;
    }

    // 发送文件路径到后端并获取执行结果
    fetch('/execute-code', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ path: filePath })
    })
    .then(response => response.text())
    .then(data => {
        displayResult(data);  // 使用新函数显示结果
    })
    .catch(error => {
        console.error('Error:', error);
        alert("无法执行代码！");
    });
}

// 显示执行结果
function displayResult(result) {
    const chatBox = document.getElementById("chat-box");
    const botMessage = document.createElement("p");
    botMessage.classList.add("bot-message");
    botMessage.textContent = `执行结果：${result}`;
    chatBox.appendChild(botMessage);
    chatBox.scrollTop = chatBox.scrollHeight;
    
    // 清空路径输入框并隐藏
    document.getElementById("file-path").value = "";
    document.getElementById("file-input-container").style.display = "none";
}


// 示例：更改功能的响应提示
function showFeatureMessage(feature) {
    const chatBox = document.getElementById("chat-box");
    const botMessage = document.createElement("p");
    botMessage.classList.add("bot-message");
    botMessage.textContent = `${feature} 功能待开发。`;
    chatBox.appendChild(botMessage);
    chatBox.scrollTop = chatBox.scrollHeight;
}

// 初始化函数，监听 DOM 内容加载完成事件
document.addEventListener("DOMContentLoaded", function() {
    console.log("页面已加载，准备开始对话...");
});

