document.addEventListener('DOMContentLoaded', function() {
    const addCommentButton = document.getElementById('add-comment');
    const newCommentInput = document.getElementById('new-comment');
    const commentsContainer = document.getElementById('comments');

    addCommentButton.addEventListener('click', function() {
        const commentText = newCommentInput.value.trim();
        if (commentText !== '') {
            addComment(commentText);
            newCommentInput.value = '';
        }
    });

    function addComment(text) {
        const commentDiv = document.createElement('div');
        commentDiv.classList.add('comment');

        const commentTextP = document.createElement('p');
        commentTextP.classList.add('comment-text');
        commentTextP.textContent = text;

        const removeButton = document.createElement('button');
        removeButton.classList.add('remove-comment');
        removeButton.textContent = 'Remove';
        removeButton.addEventListener('click', function() {
            commentDiv.remove();
        });

        commentDiv.appendChild(commentTextP);
        commentDiv.appendChild(removeButton);
        commentsContainer.appendChild(commentDiv);
    }
});