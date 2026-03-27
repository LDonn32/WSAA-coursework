const API_URL = "http://localhost:5000/books";   // Change to your API

$(document).ready(function () {
    loadBooks();

    $("#addBookBtn").click(function () {
        const newBook = {
            title: $("#title").val(),
            author: $("#author").val()
        };

        $.ajax({
            url: API_URL,
            method: "POST",
            contentType: "application/json",
            data: JSON.stringify(newBook),
            success: function () {
                $("#title").val("");
                $("#author").val("");
                loadBooks();
            }
        });
    });
});

function loadBooks() {
    $.ajax({
        url: API_URL,
        method: "GET",
        success: function (books) {
            const tbody = $("#booksTable tbody");
            tbody.empty();

            books.forEach(book => {
                tbody.append(`
                    <tr>
                        <td>${book.id}</td>
                        <td><input type="text" value="${book.title}" id="title-${book.id}"></td>
                        <td><input type="text" value="${book.author}" id="author-${book.id}"></td>
                        <td>
                            <button class="action-btn" onclick="updateBook(${book.id})">Update</button>
                            <button class="action-btn" onclick="deleteBook(${book.id})">Delete</button>
                        </td>
                    </tr>
                `);
            });
        }
    });
}

function updateBook(id) {
    const updatedBook = {
        title: $(`#title-${id}`).val(),
        author: $(`#author-${id}`).val()
    };

    $.ajax({
        url: `${API_URL}/${id}`,
        method: "PUT",
        contentType: "application/json",
        data: JSON.stringify(updatedBook),
        success: function () {
            loadBooks();
        }
    });
}

function deleteBook(id) {
    $.ajax({
        url: `${API_URL}/${id}`,
        method: "DELETE",
        success: function () {
            loadBooks();
        }
    });
}
