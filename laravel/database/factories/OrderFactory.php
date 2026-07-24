<?php

namespace Database\Factories;

use App\Models\Order;
use Illuminate\Database\Eloquent\Factories\Factory;

/**
 * @extends Factory<Order>
 */
class OrderFactory extends Factory
{
    /**
     * Define the model's default state.
     *
     * @return array<string, mixed>
     */
    public function definition(): array
    {
        return [

            'user_id'=>1,

            'product_id'=>1,

            'quantity'=>$this->faker->numberBetween(1,5),

            'total_price'=>$this->faker->numberBetween(100,10000)

        ];
    }
}
