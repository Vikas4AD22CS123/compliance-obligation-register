# Day 8 Task - Testing the Endpoints

## **1. POST /generate-report (JSON Response)**

### Using curl:
```bash
curl -X POST http://127.0.0.1:5000/generate-report \
  -H "Content-Type: application/json" \
  -d '{"text": "Company has missing compliance policies"}'
```

### Expected Response:
```json
{
  "title": "Compliance Risk Report",
  "executive_summary": "Compliance assessment for: Company has missing compliance policies. This issue requires immediate attention and proper documentation.",
  "overview": "Detailed compliance review based on submitted issue: 'Company has missing compliance policies'. The organization must ensure full adherence to regulatory requirements and internal policies.",
  "top_items": [
    "Policy gaps identified",
    "Training required",
    "Audit pending"
  ],
  "recommendations": [
    "Update compliance policies",
    "Conduct employee training",
    "Perform regular audits"
  ]
}
```

---

## **2. GET /generate-report-stream (Server-Sent Events)**

### Using curl:
```bash
curl http://127.0.0.1:5000/generate-report-stream?text=Company%20has%20missing%20compliance%20policies
```

### Expected Streaming Response:
```
data: Generating Compliance Report...

data: Title: Compliance Risk Report

data: Executive Summary: Compliance assessment for Company has missing compliance policies. This issue requires immediate attention and proper documentation.

data: Overview: Detailed compliance review based on submitted issue: 'Company has missing compliance policies'. The organization must ensure full adherence to regulatory requirements and internal policies.

data: Top Items:

data: - Policy gaps identified

data: - Training required

data: - Audit pending

data: Recommendations:

data: - Update compliance policies

data: - Conduct employee training

data: - Perform regular audits

data: Report Completed
```

---

## **3. Frontend JavaScript Example**

```javascript
// Example 1: Basic EventSource usage
const source = new EventSource("http://127.0.0.1:5000/generate-report-stream?text=test");

source.onmessage = function(event) {
    console.log(event.data);
};

source.onerror = function(event) {
    console.log("Error:", event);
    source.close();
};

// Example 2: Displaying in HTML
const source = new EventSource("http://127.0.0.1:5000/generate-report-stream?text=Company%20has%20compliance%20issues");
const reportDiv = document.getElementById("report");

source.onmessage = function(event) {
    const line = document.createElement("p");
    line.textContent = event.data;
    reportDiv.appendChild(line);
};

source.onerror = function(event) {
    console.error("Stream error:", event);
    source.close();
};
```

---

## **4. Frontend HTML Example**

```html
<!DOCTYPE html>
<html>
<head>
    <title>AI Compliance Report - Live Streaming</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        #report { border: 1px solid #ccc; padding: 15px; min-height: 200px; }
        .report-line { margin: 5px 0; }
    </style>
</head>
<body>
    <h1>Compliance Report - Live Stream</h1>
    
    <div id="report"></div>
    
    <script>
        // Connect to SSE endpoint
        const text = "Company has missing compliance policies";
        const source = new EventSource(
            `http://127.0.0.1:5000/generate-report-stream?text=${encodeURIComponent(text)}`
        );
        
        const reportDiv = document.getElementById("report");
        
        // Handle incoming messages
        source.onmessage = function(event) {
            const line = document.createElement("p");
            line.className = "report-line";
            line.textContent = event.data;
            reportDiv.appendChild(line);
        };
        
        // Handle errors
        source.onerror = function(event) {
            const line = document.createElement("p");
            line.className = "report-line";
            line.textContent = "❌ Stream Error";
            reportDiv.appendChild(line);
            source.close();
        };
    </script>
</body>
</html>
```

---

## **Key Points**

✅ **POST /generate-report** - Returns complete JSON report immediately  
✅ **GET /generate-report-stream** - Streams report line-by-line using SSE  
✅ **Query Parameter** - Pass text via URL: `?text=your%20text`  
✅ **EventSource API** - Browser's built-in SSE support (no extra libraries)  
✅ **Error Handling** - Both endpoints handle errors gracefully  
✅ **Time Delays** - Each line has a 0.5-1 second delay for demo effect  

