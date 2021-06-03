const raycaster = new THREE.Raycaster();
const mouse = new THREE.Vector2();

function onMouseMove(event) {



    mouse.x = (event.clientX / window.innerWidth) * 2 - 1;
    mouse.y = -(event.clientY / window.innerHeight) * 2 + 1;

}

function render() {


    raycaster.setFromCamera(mouse, camera);


    const intersects = raycaster.intersectObjects(scene.children);

    for (let i = 0; i < intersects.length; i++) {

        intersects[i].object.material.color.set(0xff0000);

    }

    renderer.render(scene, camera);

}

window.addEventListener('mousemove', onMouseMove, false);

window.requestAnimationFrame(render);
