document.addEventListener("DOMContentLoaded", loadStudents);

function loadStudents() {
    fetch("/api/students")
        .then(res => res.json())
        .then(data => {
            const list = document.getElementById("studentList");
            list.innerHTML = "";
            data.forEach(s => {
                list.innerHTML += `<li>${s.name} (${s.email})</li>`;
            });
        });
}

document.getElementById("addStudentForm").addEventListener("submit", function(e) {
    e.preventDefault();

    const student = {
        name: document.getElementById("name").value,
        email: document.getElementById("email").value
    };

    fetch("/api/students", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(student)
    })
    .then(() => loadStudents());
});
