const express = require('express');
const multer = require('multer');
const path = require('path');
const app = express();
const port = 8080;

const storage = multer.diskStorage({
    destination: 'data/',
    filename: (req, file, cb) => {
        const uniqueSuffix = Date.now() + '-' + Math.round(Math.random() * 1E9);
        const fileExtension = '.png';
        cb(null, uniqueSuffix + fileExtension);
    }
});

const upload = multer({ storage: storage });

app.use(express.static('public'));

app.post('/upload', upload.single('photo'), (req, res) => {
    res.json({ message: 'File uploaded successfully' });
});

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
