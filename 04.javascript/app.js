const express = require('express');
const path = require('path');

const app = express();
const port = 3000;

// 정적 파일 제공을 위한 미들웨어 등록
app.use(express.static(path.join(__dirname, '04.javascript')));
app.use(express.static(path.join(__dirname, 'css')));

// 환경설정
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, '3.project', '0.NumberGame.html'));
});

app.listen(port, (req, res) => {
    console.log(`${port}번 포트에서 실행중~!!`)
})