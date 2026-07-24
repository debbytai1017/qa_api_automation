<?php

namespace App\Http\Controllers\Api;

use App\Http\Controllers\Controller;
use App\Models\Product;
use Illuminate\Http\Request;

class ProductController extends Controller
{
    // 查詢全部
    public function index()
    {
        return Product::all();
    }

    // 新增
    public function store(Request $request)
    {
        $product = Product::create([
            'name'  => $request->name,
            'price' => $request->price,
            'stock' => $request->stock,
        ]);

        return response()->json($product, 201);
    }

    // 查詢單筆
    public function show(Product $product)
    {
        return $product;
    }

    // 更新
    public function update(Request $request, Product $product)
    {
        $product->update($request->all());

        return $product;
    }

    // 刪除
    public function destroy(Product $product)
    {
        $product->delete();

        return response()->noContent();
    }
}