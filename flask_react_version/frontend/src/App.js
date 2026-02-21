import React, { useState } from 'react';
import './App.css';

function App() {
  const [image, setImage] = useState(null);
  const [mask, setMask] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleUpload = (e) => {
    setImage(URL.createObjectURL(e.target.files[0]));
    setMask(null);
  };

  const handleSegment = async () => {
    const fileInput = document.querySelector('input[type="file"]');
    const formData = new FormData();
    formData.append('image', fileInput.files[0]);

    setLoading(true);
    const response = await fetch('http://localhost:5000/segment', {
      method: 'POST',
      body: formData,
    });
    const data = await response.json();
    setMask(`data:image/png;base64,${data.mask}`);
    setLoading(false);
  };

  return (
    <div className="App">
      <h1>Image Segmentation App</h1>
      <input type="file" accept="image/*" onChange={handleUpload} />
      <br/><br/>
      {image && (
        <button onClick={handleSegment} disabled={loading}>
          {loading ? 'Segmenting...' : 'Segment Image'}
        </button>
      )}
      <div className="results">
        {image && <img src={image} alt="Original" width={400} />}
        {mask && <img src={mask} alt="Segmented" width={400} />}
      </div>
    </div>
  );
}

export default App;