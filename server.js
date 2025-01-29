const express = require('express');
const path = require('path');
const app = express();
const morgan = require('morgan');
const port = 3000;

// 使用 morgan 记录所有请求
app.use(morgan('combined')); // 'combined' 输出格式类似于 Apache 的组合日志格式

// 设置静态文件目录
app.use(express.static(path.join(__dirname, 'public')));

// 回应消息
// app.get('/api/message', (req, res) => {
//     // 设置响应头为 JSON 类型
//     res.setHeader('Content-Type', 'application/json');
//     res.statusCode = 200;

//     // 构建 JSON 响应
//     const responseJson = {
//         message: "Hello world",
//         status: "success"
//     };

//     // 发送 JSON 响应
//     res.json(responseJson);
// });

app.get('/api/mission_info_list',(req, res)=>{
    const missionlist=[
        {
            id:1,
            institution:"中国航天",
            missionName:"长征三号乙 | 实践-25",
            launchTime:"2025/1/7 04:00",
            imageUrl:"/images/test04.jpg"
        },
        {
            id:2,
            institution:"SpaceX太空探索技术公司",
            missionName:"猎鹰9号 | 太空开拓者&新星C IM-2",
            launchTime:"2025/2/26",
            imageUrl:"/images/test05.jpg"
        },
        {
            id:3,
            institution:"中国航天（八院）",
            missionName:"长征12号R | 75km级VTVL试验",
            launchTime:"2025/1/19 11:00",
            imageUrl:"/images/test06.jpg"
        },
    ]
    res.json(missionlist);
});

// 启动服务器
app.listen(port, () => {
    console.log(`Server is running at http://localhost:${port}/`);
});