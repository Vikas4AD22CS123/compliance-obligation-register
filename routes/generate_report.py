# Flask Blueprint for generating compliance reports
from flask import Blueprint, request, jsonify

# Create a Blueprint named report_bp
report_bp = Blueprint('report_bp', __name__)


@report_bp.route('/generate-report', methods=['POST'])
def generate_report():
    """
    POST /generate-report endpoint
    
    Accepts JSON input with compliance issue details and returns
    a structured professional report.
    
    Expected JSON input:
    {
        "text": "compliance issue details"
    }
    """
    
    try:
        # Step 1: Validate that request has JSON body
        if not request.is_json:
            return jsonify({
                "error": "Request body must be JSON"
            }), 400
        
        # Step 2: Get the JSON data from request
        data = request.get_json()
        
        # Step 3: Validate that request body is not empty
        if not data:
            return jsonify({
                "error": "Request body cannot be empty"
            }), 400
        
        # Step 4: Validate that 'text' field exists
        if 'text' not in data:
            return jsonify({
                "error": "Missing required field: 'text'"
            }), 400
        
        # Step 5: Get the text and validate it's not empty
        text = data.get('text', '').strip()
        
        if not text:
            return jsonify({
                "error": "The 'text' field cannot be empty"
            }), 400
        
        # Step 6: Generate a dummy professional report based on input text
        # (In the future, this will call a real AI API)
        report = generate_dummy_report(text)
        
        # Step 7: Return the report as JSON response
        return jsonify(report), 200
    
    except Exception as e:
        # Step 8: Handle any unexpected errors
        return jsonify({
            "error": f"An error occurred: {str(e)}"
        }), 500


def generate_dummy_report(text):
    """
    Generate a dummy professional compliance report.
    
    This function creates a structured report based on the input text.
    In a real implementation, this would call an AI API to generate
    intelligent recommendations based on the compliance issue details.
    
    Args:
        text (str): The compliance issue details
        
    Returns:
        dict: A structured compliance report in the required format
    """
    
    # Extract first 100 characters for the executive summary
    summary_text = text[:100]
    
    # Create the structured report response
    report = {
        "title": "Compliance Risk Report",
        "executive_summary": f"Compliance assessment for: {summary_text}. This issue requires immediate attention and proper documentation.",
        "overview": f"Detailed compliance review based on submitted issue: '{text}'. The organization must ensure full adherence to regulatory requirements and internal policies.",
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
    
    return report
