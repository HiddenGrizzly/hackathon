const express = require('express');
const fs = require('fs');
const path = require('path');
const cors = require('cors');

const app = express();
const port = 3000;

app.use(cors());

// API endpoint to search for videos by title
app.get('/api/videos', (req, res) => {
    const title = req.query.title;
    if (!title) {
        return res.status(400).json({ error: 'Title query parameter is required' });
    }

    fs.readdir(path.join(__dirname, 'assets'), (err, files) => {
        if (err) {
            return res.status(500).json({ error: 'Failed to read assets directory' });
        }

        const videos = files.filter(file => file.toLowerCase().includes(title.toLowerCase()));
        res.json(videos);
    });
});

// Serve video files statically
app.use('/assets', express.static(path.join(__dirname, 'assets')));

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
