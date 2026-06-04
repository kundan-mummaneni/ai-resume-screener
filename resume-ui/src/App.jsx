import { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {

  const [jd, setJd] = useState(null);
  const [resume, setResume] = useState(null);
  const [result, setResult] = useState(null);

  const handleSubmit = async () => {

    const formData = new FormData();

    formData.append("jd", jd);
    formData.append("resume", resume);

    try {

      const response = await axios.post(
        "http://127.0.0.1:8000/analyze",
        formData
      );

      setResult(response.data);

    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div className="app">

      <div className="card">

        <h1>Resume Screener</h1>

        <div className="upload-section">

          <label>Job Description</label>

          <input
            type="file"
            onChange={(e) =>
              setJd(e.target.files[0])
            }
          />

          <label>Resume PDF</label>

          <input
            type="file"
            onChange={(e) =>
              setResume(e.target.files[0])
            }
          />

          <button onClick={handleSubmit}>
            Analyze Resume
          </button>

        </div>

        {result && (

          <div className="results">

            <div className="score-card">
              <h2>Match Score</h2>

              <div className="score">
                {result.final_score}%
              </div>
            </div>

            <div className="skills-grid">

              <div className="skills-box">

                <h3>Matched Skills</h3>

                <ul>
                  {(result.matched || []).map(skill => (
                    <li key={skill}>
                      ✅ {skill}
                    </li>
                  ))}
                </ul>

              </div>

              <div className="skills-box">

                <h3>Missing Skills</h3>

                <ul>
                  {(result.missing || []).map(skill => (
                    <li key={skill}>
                      ❌ {skill}
                    </li>
                  ))}
                </ul>

              </div>

            </div>

          </div>

        )}

      </div>

    </div>
  );
}

export default App;