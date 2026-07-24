<!DOCTYPE html>
<html>

<head>
    <title>Products</title>
</head>

<body>
    <h1>Product List</h1>
    <table border="1" cellpadding="8">
        <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Price</th>
            <th>Stock</th>
        </tr> @foreach($products as $product) <tr>
            <td>{{ $product->id }}</td>
            <td>{{ $product->name }}</td>
            <td>{{ $product->price }}</td>
            <td>{{ $product->stock }}</td>
        </tr> @endforeach
    </table>
</body>

</html>