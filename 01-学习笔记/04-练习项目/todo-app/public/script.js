// 页面加载时获取待办事项
window.onload = async () => {
  const response = await fetch('/api/todos');
  const todos = await response.json();
  renderTodos(todos);
};

// 渲染待办列表
function renderTodos(todos) {
  const list = document.getElementById('todo-list');
  list.innerHTML = '';
  todos.forEach(todo => {
    const li = document.createElement('li');
    li.className = `todo-item ${todo.done ? 'done' : ''}`;
    li.innerHTML = `
      <input type="checkbox" ${todo.done ? 'checked' : ''} onchange="toggleTodo(${todo.id})">
      ${todo.text}
      <button onclick="deleteTodo(${todo.id})">删除</button>
    `;
    list.appendChild(li);
  });
}

// 添加新待办
async function addTodo() {
  const input = document.getElementById('new-todo');
  const text = input.value.trim();
  if (!text) return;

  const response = await fetch('/api/todos', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ text })
  });
  
  const newTodo = await response.json();
  input.value = '';
  renderTodos([...await fetchTodos(), newTodo]);
}

// 获取最新待办列表
async function fetchTodos() {
  const res = await fetch('/api/todos');
  return await res.json();
}

// 切换完成状态（示例）
async function toggleTodo(id) {
  console.log(`切换事项 ${id} 的状态`);
  // 实际开发中这里需调用PUT API更新后端
}

// 删除待办（示例）
async function deleteTodo(id) {
  console.log(`删除事项 ${id}`);
  // 实际开发中这里需调用DELETE API
}