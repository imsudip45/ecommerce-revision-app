from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import markdown2
from datetime import datetime
import os
import uvicorn

from data import syllabus_data

app = FastAPI(title="E-commerce Course Revision", debug=True)

# Verify template directory exists
template_dir = os.path.join(os.path.dirname(__file__), "templates")
if not os.path.exists(template_dir):
    os.makedirs(template_dir)

# Mount static files (for CSS)
static_dir = os.path.join(os.path.dirname(__file__), "static")
if not os.path.exists(static_dir):
    os.makedirs(static_dir)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configure templates
templates = Jinja2Templates(directory="templates")

# Add custom template filters
def markdown_filter(text):
    return markdown2.markdown(text, extras=["break-on-newline"])

templates.env.filters["markdown"] = markdown_filter
templates.env.globals["now"] = datetime.now

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """Display the homepage with all units"""
    try:
        print("Rendering index page with units:", syllabus_data)  # Debug print
        # Convert dictionary to sorted list for display
        sorted_units = [syllabus_data[i] for i in sorted(syllabus_data.keys())]
        return templates.TemplateResponse(
            "index.html",
            {"request": request, "units": sorted_units}
        )
    except Exception as e:
        print(f"Error rendering index page: {str(e)}")  # Debug print
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/unit/{unit_id}", response_class=HTMLResponse)
async def read_unit(request: Request, unit_id: int):
    """Display detailed content for a specific unit"""
    try:
        if unit_id not in syllabus_data:
            raise HTTPException(status_code=404, detail="Unit not found")
        unit = syllabus_data[unit_id]
        print(f"Rendering unit page for unit {unit_id}:", unit)  # Debug print
        return templates.TemplateResponse(
            "unit.html",
            {
                "request": request,
                "unit_id": unit_id,
                "unit": unit
            }
        )
    except Exception as e:
        print(f"Error rendering unit page: {str(e)}")  # Debug print
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/debug")
async def debug_info():
    """Debug endpoint to check data"""
    return {
        "units_count": len(syllabus_data),
        "unit_ids": list(syllabus_data.keys()),
        "first_unit": syllabus_data[1] if 1 in syllabus_data else None,
        "template_dir_exists": os.path.exists(template_dir),
        "templates_found": os.listdir(template_dir),
        "static_dir_exists": os.path.exists(static_dir),
        "static_files": os.listdir(static_dir) if os.path.exists(static_dir) else []
    }

if __name__ == "__main__":
    print("\nStarting E-commerce Course Revision Tool...")
    print("Template directory:", template_dir)
    print("Static directory:", static_dir)
    print(f"Number of units in data: {len(syllabus_data)}")
    print("\nOnce the server starts, try these URLs:")
    print("- Main page: http://127.0.0.1:8000")
    print("- Debug info: http://127.0.0.1:8000/debug")
    print("- API docs: http://127.0.0.1:8000/docs")
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="debug") 