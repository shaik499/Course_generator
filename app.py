import streamlit as st
import os

from course_generator import generate_course

from course_storage import (
    save_course,
    load_course,
    list_courses
)

from export_utils import (
    export_pdf,
    export_docx
)

# ==========================
# CREATE FOLDERS
# ==========================

os.makedirs("generated_courses/pdf", exist_ok=True)
os.makedirs("generated_courses/docx", exist_ok=True)
os.makedirs("generated_courses/text", exist_ok=True)

# ==========================
# PAGE CONFIG
# ==========================

st.set_page_config(
    page_title="AI Course Generator",
    page_icon="🎓",
    layout="wide"
)

# ==========================
# HEADER
# ==========================

st.title("🎓 AI Course Generator")
st.caption(
    "Generate complete AI-powered courses with quizzes and assignments."
)

# ==========================
# STATS
# ==========================

total_courses = len(list_courses())

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "📚 Total Courses",
        total_courses
    )

with col2:
    st.metric(
        "🤖 AI Model",
        "Llama 3.3"
    )

# ==========================
# SIDEBAR
# ==========================

st.sidebar.title("📚 Course Library")

saved_courses = list_courses()

selected_course = st.sidebar.selectbox(
    "Saved Courses",
    [""] + saved_courses
)

if selected_course:

    course_data = load_course(selected_course)

    st.subheader(
        f"📖 {selected_course}"
    )

    st.markdown(
        course_data["content"]
    )

    st.stop()

# ==========================
# INPUTS
# ==========================

topic = st.text_input(
    "Course Topic"
)

level = st.selectbox(
    "Level",
    [
        "Beginner",
        "Intermediate",
        "Advanced"
    ]
)

duration = st.text_input(
    "Duration",
    "4 Weeks"
)

audience = st.text_input(
    "Audience",
    "College Students"
)

# ==========================
# GENERATE
# ==========================

if st.button("🚀 Generate Course"):

    if not topic.strip():

        st.warning(
            "Please enter a course topic."
        )

    else:

        with st.spinner(
            "Generating course..."
        ):

            result = generate_course(
                topic,
                level,
                duration,
                audience
            )

        # Save course
        save_course(
            topic,
            result
        )

        st.success(
            "Course generated successfully!"
        )

        st.subheader(
            "Generated Course"
        )

        st.markdown(result)

        # ==========================
        # EXPORTS
        # ==========================

        pdf_path = (
            f"generated_courses/pdf/{topic}.pdf"
        )

        docx_path = (
            f"generated_courses/docx/{topic}.docx"
        )

        export_pdf(
            result,
            pdf_path
        )

        export_docx(
            result,
            docx_path
        )

        col1, col2 = st.columns(2)

        with col1:

            with open(
                pdf_path,
                "rb"
            ) as pdf_file:

                st.download_button(
                    label="📄 Download PDF",
                    data=pdf_file,
                    file_name=f"{topic}.pdf",
                    mime="application/pdf"
                )

        with col2:

            with open(
                docx_path,
                "rb"
            ) as docx_file:

                st.download_button(
                    label="📝 Download DOCX",
                    data=docx_file,
                    file_name=f"{topic}.docx",
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                )