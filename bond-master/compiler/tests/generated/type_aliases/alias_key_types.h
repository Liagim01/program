
#pragma once

#include <bond/core/bond_version.h>

#if BOND_VERSION < 0x0902
#error This file was generated by a newer version of the Bond compiler and is incompatible with your version of the Bond library.
#endif

#if BOND_MIN_CODEGEN_VERSION > 0x0c10
#error This file was generated by an older version of the Bond compiler and is incompatible with your version of the Bond library.
#endif

#include <bond/core/config.h>
#include <bond/core/containers.h>



namespace test
{
    using String = std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<arena>::template rebind_alloc<char> >;

    using Int = int32_t;

    
    struct foo
    {
        using allocator_type = arena;

        std::map< ::test::String, ::test::Int, std::less< ::test::String>, typename std::allocator_traits<arena>::template rebind_alloc<std::pair<const ::test::String, ::test::Int> > > m;
        std::set< ::test::Int, std::less< ::test::Int>, typename std::allocator_traits<arena>::template rebind_alloc< ::test::Int> > s;
        
        template <int = 0> // Workaround to avoid compilation if not used
        foo()
        {
        }

        
        // Compiler generated copy ctor OK
        foo(const foo&) = default;
        
        foo(foo&&) = default;
        
        explicit
        foo(const arena& allocator)
          : m(allocator),
            s(allocator)
        {
        }
        
        
        // Compiler generated operator= OK
        foo& operator=(const foo&) = default;
        foo& operator=(foo&&) = default;

        bool operator==(const foo& other) const
        {
            return true
                && (m == other.m)
                && (s == other.s);
        }

        bool operator!=(const foo& other) const
        {
            return !(*this == other);
        }

        void swap(foo& other)
        {
            using std::swap;
            swap(m, other.m);
            swap(s, other.s);
        }

        struct Schema;

    protected:
        void InitMetadata(const char*, const char*)
        {
        }
    };

    inline void swap(::test::foo& left, ::test::foo& right)
    {
        left.swap(right);
    }
} // namespace test
