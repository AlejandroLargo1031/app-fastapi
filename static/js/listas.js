async function cargarLista() {
    try {
        
        const response = await fetch("/api/celulares");
        if (!response.ok) throw new Error("Error al obtener la lista de celulares");

        const datos = await response.json();
        const listaCel = document.getElementById("listaCelulares");
        listaCel.innerHTML = "";

        datos.forEach((celular) => {
            const li = document.createElement("li");
            li.textContent = `${celular.id} - ${celular.marca} - ${celular.modelo} - $${celular.precio.toFixed(2)}`;
            listaCel.appendChild(li);
        });

        const responseCli = await fetch("/api/clientes");
        if (!responseCli.ok) throw new Error("Error al obtener la lista de clientes");

        const datosCli = await responseCli.json();
        const listaCli = document.getElementById("listaClientes");
        listaCli.innerHTML = ""; 

        datosCli.forEach((clientes) => {
            const li = document.createElement("li");
            li.textContent = `${clientes.id} - ${clientes.nombre} - ${clientes.email}`;
            listaCli.appendChild(li);
        });

        const responsePro = await fetch("/api/proveedores");
        if (!responsePro.ok) throw new Error("Error al obtener la lista de listaProveedores");

        const datosPro = await responsePro.json();
        const listaPro = document.getElementById("listaProveedores");
        listaPro.innerHTML = ""; 

        datosPro.forEach((proveedor) => {
            const li = document.createElement("li");
            li.textContent = `${proveedor.id} - ${proveedor.empresa} - ${proveedor.contacto}`;
            listaPro.appendChild(li);
        });

        console.log("Lista cargada correctamente");

    } catch (error) {
        console.error("Error al cargar la listas:", error);
    }
}

async function agregarCelular(event) {
    event.preventDefault();

    console.log("Agregando celular...");
    const producto = {
        id: document.getElementById("id").value.trim(),
        marca: document.getElementById("marca").value.trim(),
        modelo: document.getElementById("modelo").value.trim(),
        precio: parseFloat(document.getElementById("precio").value)
    };

    try {
        console.log("Enviando datos:", JSON.stringify(producto));

        const response = await fetch("/api/celulares", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(producto)
        });

        const data = await response.json();

        if (!data.data) {
            throw new Error("Respuesta inválida del servidor.");
        }

        const lista = document.getElementById("listaCelulares");
        const li = document.createElement("li");
        li.textContent = `${data.data.id} - ${data.data.marca} - ${data.data.modelo} - $${data.data.precio}`;
        lista.appendChild(li);

        console.log("Celular agregado correctamente");
        
        document.getElementById("id").value = "";
        document.getElementById("marca").value = "";
        document.getElementById("modelo").value = "";
        document.getElementById("precio").value = "";

        cargarLista(); 

    } catch (error) {
        alert("Error al agregar el celular");
        console.error("Error al agregar el celular:", error);
    }
}

document.getElementById("productoForm").addEventListener("submit", agregarCelular);

document.addEventListener("DOMContentLoaded", cargarLista);
