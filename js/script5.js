const draggables = document.querySelectorAll('.draggable');
const containers = document.querySelectorAll('.container');

draggables.forEach(draggable => {
    draggable.addEventListener('dragstart', dragStart);
    draggable.addEventListener('dragend', dragEnd);
});

containers.forEach(container => {
    container.addEventListener('dragover', dragOver);
    container.addEventListener('drop', drop);
});

function dragStart(e) {
    e.dataTransfer.setData('text/plain', e.target.id);
    setTimeout(() => {
        e.target.classList.add('hide');
    }, 0);
}

function dragEnd(e) {
    e.target.classList.remove('hide');
}

function dragOver(e) {
    e.preventDefault();
    e.dataTransfer.dropEffect = 'move';
}

function drop(e) {
    e.preventDefault();
    const id = e.dataTransfer.getData('text');
    const draggable = document.getElementById(id);
    const dropTarget = e.currentTarget;
    dropTarget.appendChild(draggable);
    draggable.classList.remove('hide');
}
