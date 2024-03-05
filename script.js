const { execFile } = require('child_process');

var fileContents="";
async function resolve() {

    var input = document.getElementById("input").value;
  
    input = 'pw.live';
    input = input.trim();

    // Check if the input is empty
    if (input === "") {
      document.getElementById("result").innerText = "Please enter valid IP/domain";
       return;
    }
 
        try {
            await runPythonScript('./scan.py', [input, '-e', '1000']);
            console.log('Python ok');
        } catch (error) {
            console.error('Error running Python script:', error);
        }

        await readPorts();
    
    }

    function runPythonScript(scriptPath, args) {
        return new Promise((resolve, reject) => {
            execFile('python', [scriptPath, ...args], (error, stdout, stderr) => {
                if (error) {
                    reject(error);
                } else {
                    resolve(stdout);
                }
            });
        });
    }
    
    async function readPorts(){
        const path = require('path');
        const fs = require('fs');
    
        const filePath = path.join(__dirname, 'openports.txt');
        fs.readFile(filePath, 'utf8', (err, data) => {
            if (err) {
                console.error('Error reading the file:', err);
                return;
            }
    
            // Store the contents in a variable
            fileContents = data;
           
            console.log(fileContents);

            let result = run();

           // document.getElementById("result").innerText = result;
        });

    }

const {
    GoogleGenerativeAI,
    HarmCategory,
    HarmBlockThreshold,
  } = require("@google/generative-ai");
  
  const MODEL_NAME = "gemini-pro";
  const API_KEY = "API_KEY";
  
  async function run() {
    const genAI = new GoogleGenerativeAI(API_KEY);
    const model = genAI.getGenerativeModel({ model: MODEL_NAME });
  
    const generationConfig = {
      temperature: 0.9,
      topK: 1,
      topP: 1,
      maxOutputTokens: 2048,
    };
  
    const safetySettings = [
      {
        category: HarmCategory.HARM_CATEGORY_HARASSMENT,
        threshold: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
      },
      {
        category: HarmCategory.HARM_CATEGORY_HATE_SPEECH,
        threshold: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
      },
      {
        category: HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
        threshold: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
      },
      {
        category: HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
        threshold: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
      },
    ];
  
    const parts = [
      {text: `{open ports}${fileContents}{potential vuln and mitigations}`},
    ];
  
    const result = await model.generateContent({
      contents: [{ role: "user", parts }],
      generationConfig,
      safetySettings,
    });
  
    const response = result.response;
    console.log(response.text());
    return response;

  }
  
  //resolve();   
    
