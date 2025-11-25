const express = require('express');
const app = express();
const port = 3011;

// 允许解析JSON请求体
app.use(express.json());

// 提供静态文件（前端HTML/CSS/JS）
app.use(express.static('public'));



// 获取所有待办事项
app.get('/api/todos', (req, res) => {
  res.json(todos);
});

// 添加新待办事项
app.post('/api/todos', (req, res) => {
  const newTodo = {
    id: Date.now(), // 用时间戳作为ID
    text: req.body.text,
    done: false
  };
  todos.push(newTodo);
  res.status(201).json(newTodo);
});

async function initializeDatabase() {

try {

// 创建数据库（如果不存在）

await pool.query("CREATE DATABASE IF NOT EXISTS todo_app");

// 使用数据库

await pool.query("USE todo_app");

// 创建表

await pool.query(`

CREATE TABLE IF NOT EXISTS todos (

id INT AUTO_INCREMENT PRIMARY KEY,

text VARCHAR(255) NOT NULL,

done BOOLEAN NOT NULL DEFAULT FALSE,

created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

)

`);

console.log('Database initialized');

} catch (err) {

console.error('Database initialization failed', err);

}

}

// 在服务器启动时初始化数据库

initializeDatabase();

// 启动服务器
app.listen(port, () => {
  console.log(`后端服务运行在 http://localhost:${port}`);
});

const mysql = require('mysql2/promise');

// 创建连接池

const pool = mysql.createPool({

host: process.env.DB_HOST,

user: process.env.DB_USER,

password: process.env.DB_PASSWORD,

database: process.env.DB_DATABASE,

waitForConnections: true,

connectionLimit: 10,

queueLimit: 0

});


//路由
